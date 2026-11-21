# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: lucky · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated] (toàn bộ 1.200 YC); 3.414 đ [simulated] (trong phạm vi noi_dia + hang_nang) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Làm lại (+51,8%), 2. Xem lại (+40,7%), 3. Lương (+23,1%) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | 0,49× (toàn hệ thống mẫu); 0,22× (noi_dia), 0,69× (hang_nang), 0,38× (gồm chi phí cố định quy mô 45k YC/tháng) [simulated] | Giả lập | Trưởng phòng Tài chính |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử: Chính: 82,83%; Dùng (bỏ qua gợi ý): 27,12%; An toàn (lỗi lọt): 4,25% | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca lỗi phân loại theo Google PAIR (đồng thuận 100%), 5 ca có phương án khắc phục và event đo lường cụ thể | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | 20 nhân viên can thiệp vs 20 nhân viên đối chứng; MDE 6 điểm phần trăm; 3 luật dừng chuẩn NẾU – TRONG – THÌ – KHÔNG THÌ | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi tăng chi phí lên 6.787 đ (+51,8%); xem lại 100% kéo dài làm chi phí lên 11.743 đ – 12.516 đ (0,98× – 1,04×) [simulated] | Giả lập | Giám đốc vận hành |

**Đề xuất:** Go có điều kiện

- **Điều kiện 1:** Hoàn thiện nâng cấp cơ chế khóa chống trùng (idempotency key) và đối soát tự động dịch vụ sổ cái (khắc phục ca lỗi số 7 và 20) trước khi bắt đầu pilot.
  - *Người phụ trách:* Kỹ sư trưởng agent. *Ngày kiểm tra:* 2026-12-01.
- **Điều kiện 2:** Giám đốc vận hành phê duyệt văn bản chấp nhận đánh đổi mức chênh hiệu quả tối thiểu (MDE) là 6 điểm phần trăm (với power đạt khoảng 0,62 nếu mức chênh thực tế là 5 điểm).
  - *Người phụ trách:* Giám đốc vận hành. *Ngày kiểm tra:* 2026-12-01.
- **Điều kiện 3:** Kích hoạt đầy đủ hệ thống ghi nhận 10 event có gắn `trace_id`; sau tuần rollout đầu tiên (bước 0.10) phải thay thế số phút simulated bằng số phút đo kiểm thực tế trên giao diện.
  - *Người phụ trách:* Kỹ sư trưởng agent. *Ngày kiểm tra:* 2026-12-08.
- **Điều kiện 4:** Ban hành quy trình giảm dần tỉ lệ xem lại của nhân viên theo từng bước rollout (từ 100% xuống dưới 20%) khi tỉ lệ sửa và bỏ qua gợi ý duy trì ổn định dưới 15% để tránh đội chi phí vượt ngưỡng 12.000 đ.
  - *Người phụ trách:* Trưởng nhóm CSKH. *Ngày kiểm tra:* 2026-12-15.
