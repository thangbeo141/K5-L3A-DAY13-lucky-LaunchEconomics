# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Kim Đức Thắng (Lượt 1) · Người gắn nhãn 2: Kim Đức Thắng (Lượt 2 kiểm tra chéo) (gắn độc lập, không xem trước đáp án)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100%

## Quy tắc phân biệt cho các ca không trùng

Tỉ lệ đồng thuận đạt 100% (20/20 ca). Dưới đây là các quy tắc phân định nguyên nhân gốc để tránh nhầm lẫn:

- **Ca 6, 9 (Do người dùng, không phải Hệ thống):** Nguyên nhân gốc là khách chọn sai mục hoặc nhập sai mã vận đơn; việc agent chưa có tính năng gợi ý thông minh thuộc về phần khắc phục, không đổi bản chất lỗi từ người dùng.
- **Ca 13 (Giới hạn hệ thống):** Các nghiệp vụ ngoài phạm vi được thiết kế của trợ lý thuộc về giới hạn hệ thống, kể cả khi trợ lý phản hồi chưa mượt mà.
- **Ca 8, 15 (Hệ thống, không phải Ngầm):** Lỗi đã bộc lộ rõ ràng ra ngoài giao diện hoặc văn bản trích dẫn mà nhân viên nhìn thấy và phát hiện ngay trong phiên làm việc.
- **Ca 18 (Ngữ cảnh):** Trợ lý tính toán đúng quy định công ty, nhưng giả định "khách hàng tự hiểu cách tính trừ khấu hao" là sai lệch so với ngữ cảnh thực tế của người dùng.
- **Ca 12 (Ngầm):** Kết quả hoàn tất vẫn đúng nhưng ngầm phát sinh chi phí tăng gấp 3 lần suốt 3 tuần liên tiếp mà không có cảnh báo hệ thống; lỗi ngầm bao gồm cả bất thường về chi phí vận hành.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; kích hoạt cảnh báo khi vượt quá 2% tổng số yêu cầu trong ngày | Bổ sung module nhận diện định dạng mã sàn TMĐT và tự động tra cứu mã vận đơn LogiX tương ứng; nếu không tìm thấy, hiển thị hướng dẫn kèm hình ảnh trực quan | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát tự động mỗi giờ: phát hiện tin nhắn "đã hoàn" nhưng không có bản ghi sổ cái trạng thái ok cùng `trace_id`; ngưỡng cảnh báo: ≥ 1 ca | Chỉ gửi thông báo "đã hoàn" sau khi nhận phản hồi ghi sổ thành công từ dịch vụ sổ cái; nếu gặp lỗi HTTP 503 quá 3 lần, tự động chuyển trạng thái "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Thống kê tỉ lệ yêu cầu mở lại vì khiếu nại số tiền nhưng kiểm tra lại thấy tính đúng, tổng hợp theo tuần; ngưỡng cảnh báo: > 5% | Mẫu thông báo kết quả hoàn tiền luôn hiển thị chi tiết công thức tính minh bạch (ví dụ: Phí gốc 30.000 đ × 50% = 15.000 đ) | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với thuộc tính `reason = thieu_du_lieu`, phân loại theo loại yêu cầu | Duy trì cơ chế chuyển tiếp kèm bản tóm tắt tự động; loại bỏ hoàn toàn loại yêu cầu `quoc_te` ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra ngẫu nhiên mẫu 100 đơn hoàn mỗi tuần so với bảng giá cước hiện hành; ngưỡng cảnh báo: lệch ≥ 1% số đơn kiểm tra | Tự động xóa bộ nhớ đệm (cache) khi cập nhật bảng giá mới, đồng thời ghi rõ phiên bản bảng giá áp dụng vào metadata của `trace_id` | Kế toán trưởng |
