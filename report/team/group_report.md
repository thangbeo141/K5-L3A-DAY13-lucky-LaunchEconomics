# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: lucky
- Lớp: L3A
- Thành viên: xem [TEAM.md](../../TEAM.md) (Kim Đức Thắng - 2A202603702, thực hiện bài làm solo).

## 2. Mục tiêu và cách tiếp cận

- **Mục tiêu:** Xây dựng hồ sơ launch v0 toàn diện cho trợ lý hoàn phí giả định của LogiX-VN nhằm bảo vệ trước Hội đồng thẩm định Gate 2a, trả lời 4 câu hỏi cốt lõi:
  1. *Có đáng chạy không:* Đánh giá chi phí thực tế cho mỗi việc thành công so với chi phí nhân viên tự làm (12.000 đ).
  2. *Nhân viên có dùng không:* Đo lường các chỉ số sử dụng và thiết kế danh mục event telemetry có `trace_id`.
  3. *Khi hỏng thì sao:* Phân loại 20 ca lỗi theo khung Google PAIR và đề xuất phương án khắc phục có khả năng đo lường.
  4. *Kế hoạch pilot thiết kế thế nào:* Thiết kế thử nghiệm A/B có nhóm đối chứng song song, tính toán cỡ mẫu phân cụm và xác định các luật dừng an toàn.
- **Cách tiếp cận:** Dựa trên dữ liệu thực nghiệm gồm 1.200 yêu cầu và 1.624 lần chạy của agent, áp dụng mô hình kinh tế Cost-of-Pass và lý thuyết kiểm định A/B phân cụm để đưa ra các đề xuất dựa trên bằng chứng định lượng.

## 3. Giải pháp

- **Nhiệm vụ A (Mô hình chi phí):** Cài đặt `mo_hinh` trong `src/lab13.py`, phân tách chi phí token, tool, xem lại và làm lại. Phân tích chi phí cố định 40 triệu đ/tháng. Xem chi tiết tại [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ B (Phân tích độ nhạy):** Khảo sát 9 kịch bản biến động tham số, tìm ra các yếu tố tác động mạnh nhất và đánh giá chi phí toàn hệ thống theo các ngưỡng giới hạn số lần chạy lại. Xem chi tiết tại [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C (Bảng lỗi & Khắc phục):** Gắn nhãn độc lập 20 ca lỗi theo 5 loại của Google PAIR, đạt đồng thuận 100%, xây dựng bảng khắc phục 5 ca gắn liền với event cảnh báo và vai trò phụ trách. Xem chi tiết tại [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (Kế hoạch pilot):** Tính toán cỡ mẫu phân cụm (cluster randomization) theo nhân viên ($20$ can thiệp vs $20$ đối chứng), xác định MDE 6 điểm phần trăm, thiết lập 3 luật dừng chuẩn `NẾU – TRONG – THÌ – KHÔNG THÌ` trong file [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E (Chỉ số, Rủi ro & Hồ sơ):** Đặc tả 5 chỉ số và 10 event có `trace_id` tại [chi_so.md](chi_so.md), tổng hợp hồ sơ 1 trang tại [ho_so_launch_v0.md](ho_so_launch_v0.md) và thực hiện phản biện chéo tại [phieu_cham.md](phieu_cham.md).

## 4. Kết quả

- **Chi phí mỗi việc thành công:** Đạt **4.472 đ [simulated]**, gấp 16,28 lần hóa đơn token + tool (274,7 đ). Giờ nhân viên (làm lại 51,8% và xem lại 40,7%) chiếm tới 92,5% tổng chi phí.
- **Phạm vi tối ưu:** Thu hẹp về `noi_dia` (2.696 đ = 0,22×) và `hang_nang` (8.221 đ = 0,69×); loại bỏ hoàn toàn `quoc_te` (22.515 đ = 1,88×) và `doi_tac` (10.215 đ = 0,85×).
- **Chi phí cả hệ thống:** Giới hạn 2 lần chạy là tối ưu nhất cho toàn công ty (6.901.220 đ [simulated]).
- **Thiết kế thử nghiệm:** Chọn chia ngẫu nhiên theo nhân viên ($20 + 20$ cụm), m ≥ 299 yêu cầu/nhân viên, MDE = 0,06 (power = 0,62 ở mức 5 điểm).
- **Đề xuất cuối cùng:** **Go có điều kiện** (kèm 4 điều kiện ràng buộc về kỹ thuật, phê duyệt MDE, telemetry đo lường thực tế và lộ trình giảm xem lại). Kết quả duyệt chéo đạt **30/30 điểm**.

## 5. Khó khăn và cách xử lý

- *Khó khăn về cỡ mẫu phân cụm:* Số lượng nhân sự CSKH của công ty chỉ có 40 người, dẫn tới giới hạn tối đa $c / ICC = 20 / 0,02 = 1.000$ mẫu hiệu dụng, không đủ để phát hiện mức chênh 5 điểm phần trăm ($1.251$ mẫu).
- *Cách xử lý:* Chấp nhận đánh đổi nâng MDE lên 6 điểm phần trăm (cần 859 mẫu hiệu dụng mỗi nhánh, tương ứng $m \ge 299$ yêu cầu/nhân viên) và công khai rủi ro power giảm xuống 0,62 trong hồ sơ Gate 2a.

## 6. Tổng hợp đóng góp

- Học viên Kim Đức Thắng (MSSV: 2A202603702) đảm nhiệm 100% các phần việc của cả 4 vai trò (Viết code, Kiểm số, Gắn nhãn, Giữ hồ sơ & Phản biện). Chi tiết xem tại [TEAM.md](../../TEAM.md) và báo cáo cá nhân [2A202603702_KimDucThang.md](2A202603702_KimDucThang.md).

## 7. Hạn chế và hướng cải thiện

- *Hạn chế:* Các biến số về thời gian xem lại và làm lại hiện tại vẫn là dữ liệu giả lập (`_simulated`), chưa phản ánh hoàn toàn sự biến thiên tâm lý và tốc độ thao tác thực tế của nhân viên CSKH khi tiếp xúc với giao diện mới.
- *Hướng cải thiện:* Ngay sau giai đoạn rollout 10%, cần trích xuất dữ liệu đo thời gian thực từ các event `staff_review_decision` và `staff_rework_completed` để cập nhật lại mô hình chi phí thực tế.

## 8. Tài liệu tham khảo

- Erol et al., *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure".
- Statsmodels Documentation, `NormalIndPower` (mục `stats.power`).
