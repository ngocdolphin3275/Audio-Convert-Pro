<!-- Audio Convert Pro project overview — Vietnamese -->
<p align="center">
  <img src="assets/audio-convert-pro-logo.png" alt="Biểu tượng Audio Convert Pro" width="112">
</p>
<h1 align="center">Audio Convert Pro</h1>
<p align="center"><strong>Chuyển đổi âm thanh đơn giản. Kiểm soát rõ ràng.</strong></p>
<p align="center">
  Công cụ desktop Windows để chuyển đổi âm thanh hàng loạt, tuỳ chỉnh mã hoá
  theo định dạng và xác minh kết quả đầu ra.
</p>
<p align="center">
  <a href="https://ngocdolphincom.wordpress.com/vi/audio-convert-pro/">Trang dự án</a>
  ·
  <a href="https://github.com/ngocdolphin3275/Audio-Convert-Pro/releases">Tải xuống &amp; các phiên bản</a>
  ·
  <a href="https://github.com/ngocdolphin3275/Audio-Convert-Pro/tree/main/src">Mã nguồn ứng dụng</a>
</p>

---

## Giới thiệu

Audio Convert Pro là công cụ chuyển đổi âm thanh trên Windows với danh sách
xử lý gọn gàng và quy trình đơn giản. Thêm từng tệp hoặc quét thư mục, chọn
định dạng đầu ra và thư mục lưu, sau đó theo dõi và xác minh kết quả.

## Tính năng

- **Bảy định dạng đầu ra** — MP3, FLAC, AAC, WAV, OGG/Vorbis, M4A/AAC và ALAC.
- **Tuỳ chỉnh mã hoá** — preset tự động, bitrate thủ công hợp lệ và sample rate được lọc theo định dạng.
- **Xử lý hàng loạt** — thêm nhiều tệp, quét thư mục, kéo thả, bật/tắt từng mục và huỷ tác vụ đang chạy.
- **Xử lý tệp trùng tên** — ghi đè, bỏ qua hoặc đổi tên tệp đầu ra đã tồn tại.
- **Metadata và ảnh bìa** — giữ metadata và artwork được hỗ trợ khi định dạng đích cho phép.
- **Tiến trình và chẩn đoán** — trạng thái từng tệp, tiến trình tổng, ETA và nhật ký xử lý.
- **Xác minh đầu ra** — FFprobe kiểm tra codec, thời lượng và số kênh trước khi chấp nhận kết quả.

## Tải xuống và sử dụng

Bản phát hành mới nhất là **Audio Convert Pro 2.3.1**, gồm hai gói portable
tiếng Anh và tiếng Việt dành cho Windows x64.

| Ngôn ngữ | Gói portable |
|---|---|
| English | [Download Audio Convert Pro 2.3.1 — English](https://github.com/ngocdolphin3275/Audio-Convert-Pro/releases/download/v2.3.1/Audio-Convert-Pro-Windows-x64-EN-v2.3.1.zip) |
| Tiếng Việt | [Tải Audio Convert Pro 2.3.1 — Tiếng Việt](https://github.com/ngocdolphin3275/Audio-Convert-Pro/releases/download/v2.3.1/Audio-Convert-Pro-Windows-x64-VI-v2.3.1.zip) |

1. Tải gói ZIP theo ngôn ngữ anh muốn sử dụng.
2. Giải nén toàn bộ ZIP vào một thư mục có quyền ghi.
3. Mở thư mục đã giải nén và chạy **AudioConvertPro.exe**.
4. Giữ nguyên cấu trúc thư mục sau khi giải nén.

Gói portable đã có ứng dụng, Python runtime, CustomTkinter, TkinterDnD2,
Tcl/Tk, FFmpeg và FFprobe. Người dùng không cần cài trình cài đặt, Python
hoặc thiết lập FFmpeg riêng.

### Kiểm tra tệp tải xuống

Đối chiếu gói ZIP đã tải bằng mã SHA-256:

[Tải SHA256SUMS.txt](https://github.com/ngocdolphin3275/Audio-Convert-Pro/releases/download/v2.3.1/SHA256SUMS.txt)

## Nền tảng

- Windows 10/11, 64-bit (x64).
- Phân phối dạng thư mục portable.
- Không cần trình cài đặt.
- Hiện chưa phát hành bản macOS hoặc Linux.

## Mã nguồn và build

Hai phiên bản mã nguồn được duy trì riêng:

- [Mã nguồn tiếng Anh](src/AudioConvertPro_EN.py)
- [Mã nguồn tiếng Việt](src/AudioConvertPro_VI.py)
- [Hướng dẫn build](packaging/BUILD.md)
- [Các phiên bản build được cố định](requirements-build.txt)

Cả hai phiên bản đều giữ nguyên version ứng dụng **2.3.1**.

## Giấy phép

Mã nguồn ứng dụng được công bố trong repository nhưng bản phát hành này chưa
kèm một giấy phép riêng cho mã nguồn ứng dụng. FFmpeg và FFprobe đi kèm là
bản static Gyan.dev, được cấp phép riêng theo **GNU GPL v3 trở lên**.
CustomTkinter và TkinterDnD2 theo MIT, Pillow theo MIT-CMU và Python runtime
theo Python Software Foundation License.

Mỗi thành phần bên thứ ba vẫn tuân theo giấy phép tương ứng. Xem
[thông báo giấy phép bên thứ ba](docs/THIRD_PARTY_NOTICES.md),
[thông tin build FFmpeg](docs/FFmpeg-BUILD-INFO.txt) và
[các tệp giấy phép](third_party/licenses/).

## Liên kết dự án

- [Trang dự án tiếng Anh](https://ngocdolphincom.wordpress.com/audio-convert-pro/)
- [Trang dự án tiếng Việt](https://ngocdolphincom.wordpress.com/vi/audio-convert-pro/)
- [GitHub repository](https://github.com/ngocdolphin3275/Audio-Convert-Pro)
- [GitHub releases](https://github.com/ngocdolphin3275/Audio-Convert-Pro/releases)

---

<p align="center"><sub>Audio Convert Pro · Dự án MasterTools của NgocDolphin</sub></p>
