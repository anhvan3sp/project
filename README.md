# 🎵 MyMusic – Dự án CSDL & API nghe nhạc (Tin học 11)

## 1. Giới thiệu
**MyMusic** là dự án học tập dùng để minh họa **Cơ sở dữ liệu quan hệ** (bài 18–19–20 SGK Tin học 11).

Dự án giúp học sinh:
- Thiết kế CSDL có ý nghĩa thực tế
- Kết nối CSDL với API
- Xây dựng web nghe nhạc đơn giản
- Thấy rõ dữ liệu “sống”, không học chay

---

## 2. Công nghệ sử dụng
- **Python + FastAPI**: xây dựng API
- **MySQL (Aiven)**: lưu trữ dữ liệu
- **Google Drive (public)**: lưu file nhạc
- **HTML**: giao diện web nghe nhạc
- **GitHub**: quản lý mã nguồn

---

## 3. Mô hình dữ liệu (CSDL)
CSDL `mymusic` gồm 4 bảng:

- `nhac_si` – Nhạc sĩ
- `ca_si` – Ca sĩ
- `ban_nhac` – Bản nhạc (có link file nhạc)
- `ban_thu_am` – Quan hệ ca sĩ – bản nhạc

👉 Đây là mô hình **quan hệ nhiều – nhiều**, đúng chương trình SGK.

---

## 4. Cấu trúc project
