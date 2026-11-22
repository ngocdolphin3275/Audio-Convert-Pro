# Third-party notices

Audio Convert Pro 2.3.1 bundles third-party runtime components. Each component remains under its own license.

| Component | Bundled version | License |
|---|---:|---|
| FFmpeg / FFprobe | Gyan.dev build 2026-09-24-git-5253641e62 | GNU GPL v3 or later |
| Python runtime | 3.14.5 | Python Software Foundation License |
| CustomTkinter | 6.0.0 | MIT |
| tkinterdnd2 | 0.6.3 | MIT |
| Pillow | 12.3.0 | MIT-CMU |
| PyInstaller bootloader | 6.22.3 | GPL v2 or later with PyInstaller bootloader exception |

License texts included in third_party/licenses and in each portable package:
- GPL-3.0.txt
- Python-PSF-3.14.txt
- customtkinter-MIT.txt
- tkinterdnd2-MIT.txt
- Pillow-MIT-CMU.txt
- PyInstaller-COPYING.txt

The portable build includes Tcl/Tk runtime resources; their license terms are
kept with the runtime and are copied into the Licenses folder when present.

## FFmpeg

The FFmpeg binaries report GPL licensing and are distributed independently of
the application source. Their Gyan build information, exact version string,
FFmpeg source commit, build configuration and SHA-256 hashes are recorded in
docs/FFmpeg-BUILD-INFO.txt and docs/FFmpeg-BUILDCONF.txt.

The application source is published in this repository without an additional
license grant in this release. Do not treat the FFmpeg GPL license as a license
for the application's source code.
