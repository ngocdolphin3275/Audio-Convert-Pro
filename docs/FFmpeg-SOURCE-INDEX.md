# FFmpeg source and build index

## Bundled binary identity

The package uses the ffmpeg.exe and ffprobe.exe pair already present in the
previously tested AudioConverterPro runtime. The binaries report:

- Build label: 2026-09-24-git-5253641e62-essentials_build-www.gyan.dev
- Architecture: Windows x64
- Static build
- GPL enabled

The exact FFmpeg source commit reported by the binary is:
https://github.com/FFmpeg/FFmpeg/commit/5253641e62

Gyan's Windows build information and license statement:
https://www.gyan.dev/ffmpeg/builds/

## External libraries recorded by the binary

The bundled configuration includes the following external library families
among others: libaom, libass, libfreetype, libfribidi, libharfbuzz, libgme,
libgsm, libmp3lame, libopencore-amrnb, libopencore-amrwb, libopenjpeg,
libopenmpt, libopus, librubberband, libspeex, libsrt, libssh, libtheora,
libvidstab, libvmaf, libvo-amrwbenc, libvorbis, libvpx, libwebp, libx264,
libx265, libxvid, libzimg and libzmq.

The exact configure flags are retained in FFmpeg-BUILDCONF.txt. This index
records the binary provenance and upstream references available from the
binary and Gyan build page; it does not claim that this repository contains
a separately pinned source snapshot for every statically linked dependency.
