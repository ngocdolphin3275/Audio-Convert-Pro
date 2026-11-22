$ErrorActionPreference = 'Stop'
$RepoRoot = Split-Path -Parent $PSScriptRoot
$Version = '2.3.1'
$BuildRoot = Join-Path $RepoRoot 'build'
$ReleaseRoot = Join-Path $RepoRoot 'release_artifacts'

# Use the Python 3.14 launcher so this build script is not tied to one developer path.
$Python = Get-Command py.exe -ErrorAction SilentlyContinue
if (!$Python) { throw 'Python Launcher (py.exe) was not found. Install Python 3.14 x64.' }

& $Python.Source -3.14 -c "import sys,PyInstaller,customtkinter,tkinterdnd2,PIL; print(sys.version); print('Build dependencies: PASS')"
if ($LASTEXITCODE -ne 0) { throw 'Python 3.14 or one of the pinned build dependencies is unavailable.' }

$FfmpegDir = Join-Path $RepoRoot 'build_support\ffmpeg'
foreach ($tool in @('ffmpeg.exe','ffprobe.exe')) {
    if (!(Test-Path -LiteralPath (Join-Path $FfmpegDir $tool))) {
        throw "Missing $tool. See packaging/BUILD.md for the matching FFmpeg build provenance."
    }
}

$ExpectedFfmpegBuild = '2026-09-24-git-5253641e62'
$FfmpegVersion = (& (Join-Path $FfmpegDir 'ffmpeg.exe') -version 2>&1 | Select-Object -First 1 | Out-String).Trim()
$FfprobeVersion = (& (Join-Path $FfmpegDir 'ffprobe.exe') -version 2>&1 | Select-Object -First 1 | Out-String).Trim()
if ($FfmpegVersion -notmatch [regex]::Escape($ExpectedFfmpegBuild) -or
    $FfprobeVersion -notmatch [regex]::Escape($ExpectedFfmpegBuild)) {
    throw 'FFmpeg and FFprobe must be the matching tested Gyan build documented in docs/FFmpeg-BUILD-INFO.txt.'
}
Write-Output 'FFMPEG_PAIR_PROVENANCE=PASS'

$ExpectedFfmpegBuild = '2026-09-24-git-5253641e62'
$FfmpegVersion = (& (Join-Path $FfmpegDir 'ffmpeg.exe') -version 2>&1 | Select-Object -First 1 | Out-String).Trim()
$FfprobeVersion = (& (Join-Path $FfmpegDir 'ffprobe.exe') -version 2>&1 | Select-Object -First 1 | Out-String).Trim()
if ($FfmpegVersion -notmatch [regex]::Escape($ExpectedFfmpegBuild) -or
    $FfprobeVersion -notmatch [regex]::Escape($ExpectedFfmpegBuild)) {
    throw 'FFmpeg and FFprobe must be the matching tested Gyan build documented in docs/FFmpeg-BUILD-INFO.txt.'
}
Write-Output 'FFMPEG_PAIR_PROVENANCE=PASS'

foreach ($lang in @('EN','VI')) {
    $spec = Join-Path $RepoRoot ("packaging\AudioConvertPro-" + $lang + ".spec")
    $dist = Join-Path $BuildRoot ("dist-" + $lang.ToLower())
    $work = Join-Path $BuildRoot ("work-" + $lang.ToLower())
    & $Python.Source -3.14 -m PyInstaller --clean --noconfirm --distpath $dist --workpath $work $spec
    if ($LASTEXITCODE -ne 0) { throw "PyInstaller failed for $lang." }
    $exe = Join-Path $dist 'AudioConvertPro\AudioConvertPro.exe'
    if (!(Test-Path -LiteralPath $exe)) { throw "Expected EXE missing: $exe" }
    Write-Output ("BUILD_" + $lang + "_PASS")
}

& $Python.Source -3.14 (Join-Path $RepoRoot 'packaging\assemble_release.py')
if ($LASTEXITCODE -ne 0) { throw 'Release assembly failed.' }
Write-Output "RELEASE_ARTIFACTS: $ReleaseRoot"
