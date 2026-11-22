# Audio Convert Pro 2.3.1

Audio Convert Pro 2.3.1 is published as two Windows x64 portable editions:
English and Vietnamese.

## What's included

- Separate English and Vietnamese application sources at the same version.
- Two portable onedir packages containing the Python runtime, Tcl/Tk,
  CustomTkinter, TkinterDnD2, FFmpeg and FFprobe.
- The supplied Audio Convert Pro application icon is used for the EXE,
  application window and project branding.
- No installer or separate Python/FFmpeg installation is required.

## Reliability and format validation

- AAC/M4A sample-rate options are restricted to the tested range up to 96 kHz.
- MP3 and OGG/Vorbis manual bitrates are validated against their encoder
  constraints before FFmpeg is started.
- The ALAC source extension is included in the file picker.
- The empty-state instructions now refer to audio files rather than video.

## Verification performed

- Both Python sources compile under Python 3.14.
- Both packaged EXEs launch and remain responsive.
- English and Vietnamese UI text was inspected in actual application windows.
  Vietnamese diacritics render correctly and the inspected labels/buttons fit.
- All seven output formats passed a generated-audio conversion and FFprobe
  verification matrix with the packaged FFmpeg/FFprobe pair.
- AAC/M4A 96 kHz is accepted and 192 kHz is rejected by the format guard.
- Unsupported MP3 and OGG bitrate values are rejected before encoding.
- Both ZIP archives passed ZIP integrity checks and their SHA-256 values are
  provided in SHA256SUMS.txt.

## Downloads

- Audio-Convert-Pro-Windows-x64-EN-v2.3.1.zip
- Audio-Convert-Pro-Windows-x64-VI-v2.3.1.zip
- SHA256SUMS.txt

## Licensing

The application source is published in the repository without a separate
application license grant in this release. The bundled FFmpeg/FFprobe build
is a separate GPLv3 component. Third-party runtimes keep their own license
terms; see docs/THIRD_PARTY_NOTICES.md and third_party/licenses/.
