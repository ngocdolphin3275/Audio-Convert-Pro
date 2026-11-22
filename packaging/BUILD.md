# Build Audio Convert Pro for Windows

## Build environment

- Windows 10/11 x64
- Python 3.14.5
- PyInstaller 6.22.3
- CustomTkinter 6.0.0
- tkinterdnd2 0.6.3
- Pillow 12.3.0

The verified local environment uses Python 3.14 at:
C:\Users\Admin\AppData\Local\Programs\Python\Python314\python.exe

Install pinned build requirements using:
py -3.14 -m pip install -r requirements-build.txt

## Build both languages

Run PowerShell from the repository root:
powershell -ExecutionPolicy Bypass -File packaging\build_release.ps1

The script builds both editions sequentially with PyInstaller onedir and then
assembles portable folders and ZIP archives in release_artifacts.

Each ZIP contains AudioConvertPro.exe, the _internal runtime directory,
CustomTkinter, TkinterDnD2 and its drag-and-drop runtime, Tcl/Tk resources,
the Python runtime, FFmpeg, FFprobe, the default icon, and third-party notices
and license texts. No separate Python or FFmpeg installation is required.

## Source

- src/AudioConvertPro_EN.py
- src/AudioConvertPro_VI.py

Both source editions display version 2.3.1.

## Release QA gates

1. Both sources compile under Python 3.14.
2. Both packaged EXEs start and remain responsive.
3. English and Vietnamese labels render correctly with no broken diacritics.
4. MP3, FLAC, AAC, WAV, OGG, M4A and ALAC pass conversion and FFprobe verification.
5. AAC/M4A sample-rate restrictions and format-specific bitrate checks pass.
6. The extracted portable folder runs without a system Python or FFmpeg installation.

The bundled FFmpeg/FFprobe build is a separate GPLv3 component. See
docs/THIRD_PARTY_NOTICES.md and docs/FFmpeg-BUILD-INFO.txt.


## FFmpeg / FFprobe build input

For this release the portable packages contain the matching Gyan.dev Windows
x64 static essentials pair reported as
2026-09-24-git-5253641e62-essentials_build-www.gyan.dev. The pair is not
checked into the Git repository. To reproduce this exact package, obtain the
same upstream build and place ffmpeg.exe and ffprobe.exe in
build_support/ffmpeg/ before running the build script. The assembler refuses
to create packages if either binary is missing.

Do not substitute one executable from a different FFmpeg build. The binary
version, build configuration and SHA-256 values used for this release are
recorded in docs/FFmpeg-BUILD-INFO.txt, docs/FFmpeg-VERSION.txt and
docs/FFmpeg-BUILDCONF.txt. FFmpeg is a separate GPLv3 component; its license
text is included under third_party/licenses/.
