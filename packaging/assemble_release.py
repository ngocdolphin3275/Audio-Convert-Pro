from __future__ import annotations

import hashlib
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION = "2.3.1"
BUILD = ROOT / "build"
RELEASE = ROOT / "release_artifacts"
FFMPEG_SOURCE = ROOT / "build_support" / "ffmpeg"
LICENSE_SOURCE = ROOT / "third_party" / "licenses"

RELEASE.mkdir(parents=True, exist_ok=True)

def copy_if_exists(src: Path, dst: Path) -> None:
    if src.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    else:
        raise FileNotFoundError(f"Required release file is missing: {src}")

for lang in ("EN", "VI"):
    lang_lower = lang.lower()
    package_name = f"Audio-Convert-Pro-Windows-x64-{lang}-v{VERSION}"
    package_root = RELEASE / package_name
    if package_root.exists():
        shutil.rmtree(package_root)
    package_root.mkdir(parents=True)

    built = BUILD / f"dist-{lang_lower}" / "AudioConvertPro"
    if not (built / "AudioConvertPro.exe").is_file():
        raise FileNotFoundError(f"PyInstaller output missing: {built / 'AudioConvertPro.exe'}")
    shutil.copytree(built, package_root, dirs_exist_ok=True)

    copy_if_exists(FFMPEG_SOURCE / "ffmpeg.exe", package_root / "ffmpeg.exe")
    copy_if_exists(FFMPEG_SOURCE / "ffprobe.exe", package_root / "ffprobe.exe")
    copy_if_exists(ROOT / "assets" / "icon.ico", package_root / "icon.ico")

    readme = ROOT / "packaging" / "readmes" / f"README_{lang}.txt"
    notices = ROOT / "packaging" / "readmes" / f"THIRD_PARTY_NOTICES_{lang}.txt"
    copy_if_exists(readme, package_root / "README.txt")
    copy_if_exists(notices, package_root / "THIRD_PARTY_NOTICES.txt")
    copy_if_exists(ROOT / "docs" / "FFmpeg-BUILD-INFO.txt", package_root / "FFmpeg-BUILD-INFO.txt")

    licenses = package_root / "Licenses"
    licenses.mkdir(exist_ok=True)
    for license_file in LICENSE_SOURCE.glob("*"):
        if license_file.is_file():
            shutil.copy2(license_file, licenses / license_file.name)

    # Keep the built-in Tcl/Tk license terms available with this portable package.
    for folder in ("_tk_data", "_tcl_data"):
        for rel in (f"{folder}/license.terms",):
            src = package_root / "_internal" / rel
            if src.is_file():
                shutil.copy2(src, licenses / ("TclTk-" + folder + "-license.terms"))

    zip_path = RELEASE / f"{package_name}.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=1, allowZip64=True) as zf:
        for file in sorted(package_root.rglob("*")):
            if file.is_file():
                arcname = Path(package_name) / file.relative_to(package_root)
                zf.write(file, arcname.as_posix())
    print(f"PACKAGED {lang}: {zip_path.name} ({zip_path.stat().st_size:,} bytes)")

checksums = []
for lang in ("EN", "VI"):
    name = f"Audio-Convert-Pro-Windows-x64-{lang}-v{VERSION}.zip"
    target = RELEASE / name
    h = hashlib.sha256()
    with target.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    checksums.append(f"{h.hexdigest().upper()}  {name}")
(RELEASE / "SHA256SUMS.txt").write_text("\n".join(checksums) + "\n", encoding="utf-8", newline="\n")
print("SHA256SUMS.txt written")
