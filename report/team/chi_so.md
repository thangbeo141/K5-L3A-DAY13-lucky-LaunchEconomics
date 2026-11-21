# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: Tỉ lệ yêu cầu của nhóm can thiệp được mở trợ lý | Số yêu cầu nhóm can thiệp có event `agent_suggestion_shown` chia tổng số yêu cầu nhóm can thiệp nhận | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ đơn hoàn sai tiền qua kiểm toán mẫu | Số đơn phát hiện sai lệch số tiền qua kiểm tra đối soát ngẫu nhiên chia tổng số mẫu kiểm tra hàng tuần | Không cần tính |

*Ghi chú quan trọng:* Chỉ số trong đợt chạy thử ghi nhận là 82,83%; không viết "trợ lý đã nâng chỉ số lên 82,83%" vì đợt chạy thử 2 tuần trước đó chưa có nhóm đối chứng song song.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent. Danh sách 10 event chuẩn:

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Khách hàng (App/Web) | `request_id`, `loai`, `so_tien`, `arm`, `trace_id` | Khi khách hàng gửi yêu cầu hoàn phí |
| `agent_run_completed` | Agent backend | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Ngay khi agent hoàn tất 1 lần chạy (kể cả lỗi) |
| `agent_suggestion_shown` | Giao diện CSKH | `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý xử lý của agent hiện lên màn hình |
| `staff_review_decision` | Nhân viên CSKH | `quyet_dinh` (giu/sua/bo), `phut_xem_lai`, `trace_id` | Khi nhân viên xác nhận lựa chọn xử lý |
| `staff_rework_completed` | Nhân viên CSKH | `phut_lam_lai`, `ly_do`, `trace_id` | Khi nhân viên hoàn thành xử lý thủ công lại |
| `refund_ledger_write` | Dịch vụ sổ cái kế toán | `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi gọi lệnh ghi bút toán hoàn tiền vào sổ cái |
| `handoff_to_staff` | Agent backend | `reason`, `tom_tat`, `trace_id` | Khi agent chuyển ca khó sang nhân viên |
| `ticket_closed` | Hệ thống Helpdesk | `closed_at`, `status`, `trace_id` | Khi yêu cầu được đánh dấu đóng hoàn tất |
| `ticket_reopened` | Khách hàng | `reopened_at`, `reason`, `trace_id` | Khi khách hàng mở lại khiếu nại trong 7 ngày |
| `audit_sample_checked` | Kế toán viên đối soát | `so_tien_da_hoan`, `so_tien_chuan`, `lech`, `trace_id` | Khi kiểm tra ngẫu nhiên mẫu đơn hàng tuần |

**Kiểm tra chéo:**
- Chỉ số chính `% đóng trong 24h và không mở lại trong 7 ngày` tính từ cặp event: `ticket_closed` (tính thời gian đóng so với `refund_request_created`) và không có event `ticket_reopened` trong 7 ngày sau đó.
- Chỉ số dùng `Tỉ lệ bỏ qua gợi ý` tính từ event `staff_review_decision` (lọc theo các giá trị `quyet_dinh in ['sua', 'bo']` trên tổng số event có gợi ý).
- Chỉ số an toàn `Tỉ lệ lỗi lọt đến khách` tính từ sự xuất hiện của event `ticket_reopened`.
- Chỉ số dùng đề xuất tính từ event `agent_suggestion_shown`.
- Chỉ số an toàn đề xuất tính từ event `audit_sample_checked`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng +51,8%, lên 6.787 đ [simulated] | Tỉ lệ ca làm lại theo tuần vượt quá 7,0% (mức chạy thử là 4,9% trong phạm vi) | Thu hẹp phạm vi về chỉ xử lý `noi_dia`, rà soát 20 trace lỗi làm lại gần nhất | PM trợ lý hoàn phí |
| Duy trì xem lại 100% kéo dài | Chi phí lên tới 11.743 đ [simulated] (0,98×) đến 12.516 đ [simulated] (1,04×) | Tỉ lệ yêu cầu cần xem lại vẫn duy trì > 50% ở cuối bước rollout 0.25 | Thực hiện cắt giảm tỉ lệ xem lại theo bậc nếu tỉ lệ sửa + bỏ duy trì < 15% | Trưởng nhóm CSKH |
| Khối lượng xử lý thực tế giảm một nửa | Chi phí cố định tăng thêm 2.370 đ/việc, tổng chi phí lên 5.784 đ [simulated] (0,48×) | Số lượng yêu cầu thành công đạt dưới 50% kế hoạch trong 2 tuần | Tạm dừng mở rộng quy mô, thương lượng lại mức phí bản quyền cố định | Giám đốc vận hành |
