<!-- Audio Convert Pro project overview -->
<p align="center">
  <img src="assets/audio-convert-pro-logo.png" alt="Audio Convert Pro logo" width="112">
</p>
<h1 align="center">Audio Convert Pro</h1>
<p align="center"><strong>Simple audio conversion. Clear control.</strong></p>
<p align="center">
  A focused Windows desktop utility for batch audio conversion, format-aware
  encoding options and verified output.
</p>
<p align="center">
  <a href="https://ngocdolphincom.wordpress.com/audio-convert-pro/">Project website</a>
  ·
  <a href="https://github.com/ngocdolphin3275/Audio-Convert-Pro/releases">Downloads &amp; releases</a>
  ·
  <a href="https://github.com/ngocdolphin3275/Audio-Convert-Pro/tree/main/src">Application source</a>
</p>

---

## About

Audio Convert Pro is a Windows desktop audio converter built around a compact
queue and a straightforward workflow. Add individual files or scan folders,
choose an output format and destination, then monitor and verify the results.

## Features

- **Seven output formats** — MP3, FLAC, AAC, WAV, OGG/Vorbis, M4A/AAC and ALAC.
- **Encoding controls** — automatic presets, supported manual bitrate values and format-aware sample-rate options.
- **Batch processing** — add multiple files, scan folders, drag and drop, enable or disable queue items and cancel an active operation.
- **File conflict handling** — overwrite, skip or rename existing output files.
- **Metadata and artwork** — preserve supported source metadata and cover artwork where the target format allows it.
- **Progress and diagnostics** — per-file status, progress, overall progress, ETA and processing logs.
- **Output verification** — FFprobe checks the output codec, duration and channel count before the result is accepted.

## Download and run

The latest release is **Audio Convert Pro 2.3.1**, with separate English and
Vietnamese portable packages for Windows x64.

| Edition | Portable package |
|---|---|
| English | [Download Audio Convert Pro 2.3.1 — English](https://github.com/ngocdolphin3275/Audio-Convert-Pro/releases/download/v2.3.1/Audio-Convert-Pro-Windows-x64-EN-v2.3.1.zip) |
| Vietnamese | [Tải Audio Convert Pro 2.3.1 — Tiếng Việt](https://github.com/ngocdolphin3275/Audio-Convert-Pro/releases/download/v2.3.1/Audio-Convert-Pro-Windows-x64-VI-v2.3.1.zip) |

1. Download the ZIP for your preferred language.
2. Extract the complete ZIP to a writable folder.
3. Open the extracted folder and run **AudioConvertPro.exe**.
4. Keep the extracted folder structure intact.

The portable package contains the application, Python runtime, CustomTkinter,
TkinterDnD2, Tcl/Tk resources, FFmpeg and FFprobe. No installer, separate Python
installation or additional FFmpeg setup is needed.

### Verify your download

Compare the downloaded ZIP with the published SHA-256 checksums:

[Download SHA256SUMS.txt](https://github.com/ngocdolphin3275/Audio-Convert-Pro/releases/download/v2.3.1/SHA256SUMS.txt)

## Platform

- Windows 10/11, 64-bit (x64).
- Portable folder distribution.
- No installer required.
- macOS and Linux builds are not currently published.

## Source code and build

The English and Vietnamese application sources are maintained separately:

- [English source](src/AudioConvertPro_EN.py)
- [Vietnamese source](src/AudioConvertPro_VI.py)
- [Build instructions](packaging/BUILD.md)
- [Pinned build requirements](requirements-build.txt)

Both editions retain application version **2.3.1**.

## Licensing

The application source is published in this repository without a separate
application license grant in this release. The bundled FFmpeg and FFprobe
binaries are a separate static Gyan.dev build licensed under **GNU GPL v3 or
later**. CustomTkinter and TkinterDnD2 are MIT-licensed, Pillow uses MIT-CMU,
and the Python runtime uses the Python Software Foundation License.

Third-party components retain their own licenses. See
[Third-party notices](docs/THIRD_PARTY_NOTICES.md),
[FFmpeg build information](docs/FFmpeg-BUILD-INFO.txt) and the
[license files](third_party/licenses/).

## Project links

- [English project page](https://ngocdolphincom.wordpress.com/audio-convert-pro/)
- [Vietnamese project page](https://ngocdolphincom.wordpress.com/vi/audio-convert-pro/)
- [GitHub repository](https://github.com/ngocdolphin3275/Audio-Convert-Pro)
- [GitHub releases](https://github.com/ngocdolphin3275/Audio-Convert-Pro/releases)

---

<p align="center"><sub>Audio Convert Pro · A MasterTools project by NgocDolphin</sub></p>
