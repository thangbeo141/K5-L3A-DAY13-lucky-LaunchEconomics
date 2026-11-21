# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): lucky (Lớp L3A)
- Nhóm được chấm: MVQ (Lớp L3A - repo: trmanh204/K5-L3A-DAY13-MVQ-LaunchEconomics)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất "Go có điều kiện" rất trung thực và minh bạch: nêu rõ con số bất lợi của `quoc_te` (22.515 đ = 1,88× so với 12.000 đ `[simulated]`) để loại khỏi pilot; chỉ ra kịch bản xem lại 100% có chi phí lên tới 11.743–12.415 đ `[simulated]` (0,98×–1,03×); thừa nhận đánh đổi MDE 6 điểm khiến power giảm còn 0,642 ở mức 5 điểm; đi kèm 4 điều kiện ràng buộc có vai trò và ngày kiểm tra cụ thể. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | 100% con số tính từ cột giả lập đều có gắn nhãn `[simulated]`. Phạm vi thu hẹp rõ ràng chỉ gồm `noi_dia` (2.696 đ = 0,22×) và `hang_nang` (8.221 đ = 0,69× `[simulated]`), có phân tích chi phí cố định 40 triệu/tháng (4.599 đ ở quy mô 45k YC và 5.784 đ ở nửa khối lượng `[simulated]`). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Thiết kế tách tác động chặt chẽ: đối chứng song song 20 nhân viên can thiệp vs 20 nhân viên đối chứng tại 12 depot (seed 20261121); tính cỡ mẫu phân cụm đầy đủ (`DE = 6,96`, $m = 299$ YC/người, 859 hiệu dụng); 4 luật dừng chuẩn cú pháp NẾU – TRONG – THÌ – KHÔNG THÌ có ngưỡng định lượng, thời hạn xử lý và chức danh có quyền dừng rõ ràng (Giám đốc vận hành, Kế toán trưởng, Trưởng nhóm CSKH). |
| **Tổng** | | | | **30 / 30** | Hồ sơ của nhóm MVQ xuất sắc, lập luận chặt chẽ, số liệu chuẩn xác và thiết kế thử nghiệm rất thực tế. |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Kế hoạch pilot của nhóm MVQ giải quyết trọn vẹn cả 4 câu hỏi cốt lõi của Gate 2a. Đề xuất có căn cứ kinh tế vững chắc (tối ưu toàn hệ thống ở mức 2 lần chạy: 6.901.220 đ `[simulated]`), kiểm soát chặt chẽ rủi ro an toàn giao dịch (sửa lỗi sổ cái ca 7 và hoàn trùng ca 20) và có phương án dự phòng rollback 30 phút rõ ràng.

**Một câu hỏi cho đội trình:** "Kế hoạch pilot của nhóm duy trì xem lại 100% trong toàn bộ kỳ đo chính (07–27/12/2026), khiến chi phí dự kiến lên tới 11.743 đ – 12.415 đ/việc `[simulated]` (sát hoặc vượt mức 12.000 đ của nhân viên tự làm). Nếu dữ liệu đo thực tế ở tuần đầu cho thấy chi phí thực sự vượt 12.000 đ, nhóm sẽ kích hoạt luật dừng tài chính hay chấp nhận bù lỗ chi phí để giữ tính toàn vẹn của can thiệp đo lường?"

**Câu trả lời của đội trình (ghi lại tại buổi):** "Đội trình MVQ giải trình rằng theo Luật dừng số 3 trong `pilot_plan.yaml`, nếu chi phí mỗi việc thành công thực đo vượt quá 12.000 đ trong 2 báo cáo tuần liên tiếp (mỗi báo cáo có ≥ 100 yêu cầu), Giám đốc vận hành sẽ ngay lập tức dừng nhận ca mới trong 1 ngày và PM phải lập lại phương án tối ưu trước khi xin cấp phép pilot mới. Nhóm ưu tiên kỷ luật tài chính của công ty lên hàng đầu, đồng thời sẽ tận dụng hai bước rollout đầu (10% và 25%) để tối ưu thao tác xem lại của nhân viên xuống dưới ngưỡng hoà vốn 4,8 phút/ca."
