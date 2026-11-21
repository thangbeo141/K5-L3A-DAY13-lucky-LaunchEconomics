# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): lucky (đóng vai trò Hội đồng thẩm định độc lập Gate 2a)
- Nhóm được chấm: lucky (tự thẩm định phản biện chéo bài làm solo)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất "Go có điều kiện" nêu thẳng các con số bất lợi: `quoc_te` đắt 1,88× so với 12.000 đ [simulated], xem lại 100% đắt tới 12.516 đ (1,04×) [simulated], power chỉ đạt 0,62 ở mức 5 điểm; đi kèm giải pháp loại bỏ `quoc_te` và lộ trình giảm xem lại. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Toàn bộ các con số chi phí, thời gian xem/làm lại đều có gắn nhãn `simulated`. Phạm vi thu hẹp về `noi_dia` (0,22×) và `hang_nang` (0,69×) được chứng minh rõ ràng bằng bảng số liệu A3. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Tách tác động bằng đối chứng song song 20 nhân viên can thiệp vs 20 nhân viên đối chứng tại 12 depot; cỡ mẫu phân cụm tính đủ với MDE 6 điểm; 3 luật dừng chuẩn cú pháp NẾU – TRONG – THÌ – KHÔNG THÌ có ngưỡng, thời hạn và vai trò cụ thể. |
| **Tổng** | | | | **30 / 30** | Hồ sơ mẫu mực, minh bạch về mặt kinh tế và an toàn vận hành. |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Kế hoạch pilot được thiết kế khoa học, tách được tác động nhân quả, minh bạch về rủi ro chi phí (yếu tố làm lại và xem lại chiếm 92,5% tổng chi phí) và có các chốt an toàn dừng khẩn cấp trước khi rủi ro tài chính hoặc lỗi lọt khách hàng lan rộng.

**Một câu hỏi cho đội trình:** "Chi phí mỗi việc thành công sẽ là bao nhiêu nếu trong những tuần đầu tiên bắt buộc phải xem lại 100% các yêu cầu hoàn phí?"

**Câu trả lời của đội trình (ghi lại tại buổi):** "Nếu xem lại 100% trong phạm vi `noi_dia` + `hang_nang`, chi phí mỗi việc thành công sẽ tăng vọt lên **11.743 đ [simulated] (0,98×)** nếu mỗi ca làm lại mất 9 phút, hoặc **12.516 đ [simulated] (1,04×)** nếu thời gian làm lại thực tế là 16,2 phút như dữ liệu trace. Khi đó, trợ lý hoàn toàn không tiết kiệm được chi phí, thậm chí đắt hơn nhân viên tự làm (12.000 đ). Do đó, nhóm đặt điều kiện bắt buộc phải triển khai cơ chế giảm dần tỉ lệ xem lại theo từng bước rollout khi tỉ lệ nhân viên sửa và bỏ qua gợi ý duy trì ổn định dưới 15%."
