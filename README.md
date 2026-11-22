<!--
Audio Convert Pro project overview.
Product information is aligned with the official NgocDolphin project pages.
-->

<h1 align="center">Audio Convert Pro</h1>
<p align="center"><strong>Flexible audio conversion. Clear controls. Reliable batch processing.</strong></p>
<p align="center">
  A Windows desktop audio converter for common compressed and lossless formats.
</p>
<p align="center">
  <a href="https://ngocdolphincom.wordpress.com/audio-convert-pro/">Project website (English)</a>
  ·
  <a href="https://ngocdolphincom.wordpress.com/vi/audio-convert-pro/">Trang dự án (Tiếng Việt)</a>
  ·
  <a href="https://github.com/ngocdolphin3275/Audio-Convert-Pro">GitHub repository</a>
</p>

---

## About

Audio Convert Pro is a Windows desktop utility for converting audio files in batches. It brings format selection, practical quality controls, metadata handling and file-conflict options into one straightforward workflow.

Choose an output format, adjust bitrate and sample rate when those settings apply, add files or scan a folder, and let the conversion queue handle the selected tasks.

The project belongs to **MasterTools**, NgocDolphin's collection of open-source utility projects. It is separate from the proprietary PyProjects applications.

## Features

- **Seven output formats** — MP3, FLAC, AAC, WAV, OGG, M4A and ALAC.
- **Bitrate controls** — automatic format-specific settings or 128, 192, 256 and 320 kbps presets where applicable.
- **Sample-rate controls** — Auto, 44.1, 48, 88.2, 96, 176.4 and 192 kHz, subject to format-specific limits.
- **Lossless presets** — FLAC, WAV and ALAC use their appropriate lossless encoding paths rather than a lossy bitrate setting.
- **Metadata handling** — carry source metadata into the converted output.
- **Embedded artwork** — retain cover artwork for supported output formats, including MP3, FLAC, M4A and ALAC.
- **Batch conversion** — add individual files, scan folders recursively, enable or disable queued tasks, and cancel a running conversion.
- **Output conflict policy** — overwrite an existing output, skip it, or generate a renamed output file.
- **Progress and logs** — review file-level status, conversion progress, the overall progress bar and processing messages.
- **Drag and drop** — optional desktop drag-and-drop support when `tkinterdnd2` is installed.
- **Output verification** — use FFprobe to inspect the generated file and check key properties such as codec and duration.

## Supported formats

### Output formats

| Format | Encoding path |
|---|---|
| MP3 | MP3 encoding with configurable bitrate or automatic quality |
| FLAC | Lossless FLAC |
| AAC | AAC encoding |
| WAV | PCM audio, with source sample type/bit depth considered |
| OGG | Vorbis encoding |
| M4A | AAC in an M4A container |
| ALAC | Lossless Apple ALAC |

### Source file extensions

MP3, FLAC, WAV, M4A, M4B, AAC, OGG, OGA, Opus, WMA, ALAC, WavPack, AIFF and APE.

## Quality settings

The application provides format-aware defaults:

- **MP3** — automatic LAME V0 quality; selectable bitrate presets; sample rates of Auto, 44.1 kHz or 48 kHz.
- **FLAC** — lossless encoding with a high compression-level preset.
- **AAC** — automatic AAC VBR or a selected bitrate.
- **M4A** — AAC VBR inside the M4A container.
- **ALAC** — lossless Apple ALAC encoding.
- **WAV** — PCM output that considers the source sample type and bit depth.
- **OGG** — automatic Vorbis VBR quality or a selected bitrate.

The available options change with the selected output format so that incompatible settings are not offered.

## Batch workflow

1. Add audio files or choose a folder to scan recursively.
2. Select the output format and the available quality settings.
3. Choose an output folder.
4. Set how existing files should be handled: overwrite, skip or rename.
5. Enable the files to process and start the queue.
6. Follow the progress and log, or cancel the current operation when necessary.

The application keeps file scanning and conversion work off the main UI thread so the interface can continue responding during longer jobs.

## Requirements

- Windows desktop environment.
- Python with the standard Tkinter GUI module for running from source.
- The `customtkinter` package.
- FFmpeg and FFprobe available through the system PATH or beside the application (a `bin` subfolder is also checked).
- `tkinterdnd2` is optional and is only needed for drag-and-drop integration.

Install the required Python UI package:

```powershell
python -m pip install customtkinter
```

For optional drag-and-drop support:

```powershell
python -m pip install tkinterdnd2
```

## Source and project status

This repository is the public project home for Audio Convert Pro. The project overview is being published first; the application source files and reproducible setup instructions are not yet present in this repository.

The current project source identifies the application as **Audio Convert Pro 2.3.1**. This is a source-version reference, not a statement that a matching GitHub release asset is available.

## Platform

- Windows desktop application.
- Uses FFmpeg and FFprobe for local audio conversion and output inspection.
- No macOS or Linux build is currently documented.

## Licensing

Audio Convert Pro is intended to be an open-source MasterTools project. **A project-level LICENSE file has not yet been published in this repository.** Until an explicit license is added, the repository's public visibility should not be interpreted as permission to reuse, modify or redistribute its code.

Third-party components, including FFmpeg and optional Python packages, remain subject to their own licenses and notices. Those notices must accompany the corresponding source and binary distributions when they are published.

## Project links

- [Audio Convert Pro — English project page](https://ngocdolphincom.wordpress.com/audio-convert-pro/)
- [Audio Convert Pro — Vietnamese project page](https://ngocdolphincom.wordpress.com/vi/audio-convert-pro/)
- [NgocDolphin — independent software projects](https://ngocdolphincom.wordpress.com/)
- [MasterTools on GitHub](https://github.com/ngocdolphin3275)

---

<p align="center"><sub>Audio Convert Pro · A MasterTools project by NgocDolphin</sub></p>
