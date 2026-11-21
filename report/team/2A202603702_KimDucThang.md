# Báo cáo cá nhân — KimDucThang-2A202603702

## 1. Thông tin thành viên

- Họ tên: Kim Đức Thắng
- MSSV: 2A202603702
- Email: thangtobeo141@gmail.com
- Vai trong nhóm: Đảm nhiệm toàn bộ 4 vai trò (Người viết code, Người kiểm số, Người gắn nhãn 1, Người gắn nhãn 2 kiêm giữ hồ sơ) do thực hiện bài làm độc lập (solo).

## 2. Phần việc phụ trách

- Hoàn thiện toàn bộ bài làm Lab 13:
  - Viết code mô phỏng chi phí và kiểm thử 3 phép thử đáp án biết trước (A1).
  - Phân tích chi phí thực tế cho mỗi việc thành công trên 1.200 yêu cầu và 1.624 lần chạy của agent (A2, A3, A4).
  - Khảo sát độ nhạy qua 9 kịch bản đơn, 1 kịch bản cặp và kịch bản xem lại 100% (B1 - B4).
  - Gắn nhãn 20 ca lỗi theo 5 loại lỗi của Google PAIR và đề xuất biện pháp khắc phục định lượng (C).
  - Tính toán cỡ mẫu phân cụm (ICC = 0,02, DE = 6,96) và soạn thảo kế hoạch pilot chi tiết (D).
  - Đặc tả hệ thống chỉ số, rủi ro kinh tế và xây dựng hồ sơ duyệt Gate 2a (E).

## 3. Đóng góp cụ thể

- Tự tay cài đặt và hoàn thiện file `src/lab13.py`, đảm bảo vượt qua 3 assert kiểm tra với độ chính xác cao.
- Phân tích và phát hiện loại yêu cầu `quoc_te` (1,88× so với 12.000 đ) và `doi_tac` (0,85×) không tối ưu về mặt kinh tế, từ đó đề xuất thu hẹp phạm vi pilot về `noi_dia` (0,22×) và `hang_nang` (0,69×).
- Nhận diện 3 yếu tố rủi ro kinh tế nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), và lương nhân viên (+23,1%).
- Soạn thảo đầy đủ 3 luật dừng cho pilot theo đúng cú pháp NẾU – TRONG – THÌ – KHÔNG THÌ.
- Tuân thủ nghiêm ngặt các quy tắc: gắn nhãn `simulated` cho toàn bộ các số liệu giả lập, không sử dụng thuật ngữ chạy chính thức (chỉ duyệt pilot), gán trách nhiệm cho các vai trò cụ thể.

## 4. Bằng chứng

- File mã nguồn: `src/lab13.py` chạy qua 3 bài test A1 (1,20 · 1,25 · 1,25) và xuất đủ bảng số liệu.
- Các tài liệu hồ sơ trong `report/team/`:
  - `bang_chi_phi.md`
  - `bang_loi.md`
  - `pilot_plan.yaml`
  - `chi_so.md`
  - `ho_so_launch_v0.md`
  - `phieu_cham.md`
  - `group_report.md`

## 5. Công cụ AI đã dùng

- **Trợ lý AI:** Sử dụng Antigravity (Gemini) hỗ trợ tra cứu công thức thống kê cỡ mẫu, rà soát tính hợp lệ của cú pháp YAML, kiểm tra chéo các ràng buộc về quy tắc nộp bài (rubric).
- **Cách tự kiểm tra:** Chạy lệnh `python lab13.py` để xác thực lại toàn bộ các con số thực nghiệm so với tài liệu hướng dẫn và đảm bảo độ lệch < 2%; dùng `yaml.safe_load` để xác nhận file YAML hợp lệ.

## 6. Tự đánh giá

- Mức độ hoàn thành: 100% khối lượng công việc của cả nhóm.
- Đánh giá: Đạt đầy đủ các tiêu chí trong Rubric (70 điểm đối chiếu và 30 điểm hội đồng).
