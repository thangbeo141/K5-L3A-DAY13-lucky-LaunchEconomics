"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd
from statsmodels.stats.power import NormalIndPower

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs)
    )


def tinh_co_mau(p1, p2, alpha=0.05, power=0.8):
    """Tính cỡ mẫu cho 2 tỷ lệ độc lập."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)

    print('=== A1 · KIỂM TRA PHÉP THỬ ===')
    kiem_tra_dap_an_biet_truoc()

    print('\n=== A2 · MÔ HÌNH CHI PHÍ TỪ TRACE ===')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:15s}: {gia_tri:>14,.1f}')

    print(f"Tỉ lệ CPS / Hoá đơn: {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.2f} lần")
    print(f"Tỉ trọng làm lại: {ket_qua['lam_lai'] / ket_qua['tong'] * 100:.1f}%")
    print(f"Tỉ trọng xem lại: {ket_qua['xem_lai'] / ket_qua['tong'] * 100:.1f}%")

    print('\n=== A3 · TÁCH THEO LOẠI YÊU CẦU ===')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub_reqs = reqs[reqs['loai'] == loai]
        kq_loai = mo_hinh(runs, sub_reqs)
        so_yc = len(sub_reqs)
        tl_tc = (sub_reqs['ket_qua'] == 'thanh_cong').mean() * 100
        lan_chay_tb = sub_reqs['so_lan_chay'].mean()
        cps = kq_loai['cps']
        so_voi_12k = cps / BASELINE
        print(f"{loai:10s} | YC: {so_yc:4d} | Thành công: {tl_tc:5.1f}% | Lần chạy: {lan_chay_tb:.2f} | CPS: {cps:8,.0f} đ | So 12k: {so_voi_12k:.2f}x")

    print('\n=== A4 · CHI PHÍ CỐ ĐỊNH (noi_dia + hang_nang) ===')
    sub_dn = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_dn = mo_hinh(runs, sub_dn)
    tc_dn = kq_dn['thanh_cong']
    tong_yc_dn = len(sub_dn)
    print(f"Phạm vi noi_dia + hang_nang: {tong_yc_dn} YC, thành công: {tc_dn}, CPS: {kq_dn['cps']:,.0f} đ")
    # Ở 45.000 YC/tháng
    tc_thang_full = 45000 * tc_dn / 1200
    cp_cd_moi_viec_full = 40_000_000 / tc_thang_full
    cps_full = kq_dn['cps'] + cp_cd_moi_viec_full
    print(f"45.000 YC/tháng: Thành công/tháng: {tc_thang_full:,.0f} | Cố định/việc: {cp_cd_moi_viec_full:,.0f} đ | CPS + CĐ: {cps_full:,.0f} đ ({cps_full/BASELINE:.2f}x)")
    # Ở một nửa khối lượng (22.500 YC/tháng)
    tc_thang_half = tc_thang_full / 2
    cp_cd_moi_viec_half = 40_000_000 / tc_thang_half
    cps_half = kq_dn['cps'] + cp_cd_moi_viec_half
    print(f"Một nửa khối lượng: Thành công/tháng: {tc_thang_half:,.0f} | Cố định/việc: {cp_cd_moi_viec_half:,.0f} đ | CPS + CĐ: {cps_half:,.0f} đ ({cps_half/BASELINE:.2f}x)")

    print('\n=== B1 · BẢNG ĐỘ NHẠY (9 kịch bản) ===')
    goc = ket_qua['cps']
    kich_ban = {
        'Gốc (A2)':                   dict(),
        'Giá token gấp đôi':          dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':     dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi':      dict(he_so_xem_lai=2.0),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi':      dict(he_so_lam_lai=2.0),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%':   dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần':  dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':             dict(max_lan_chay=1),
    }
    for ten, kw in kich_ban.items():
        res = mo_hinh(runs, reqs, **kw)
        cps_kb = res['cps']
        diff = (cps_kb / goc - 1) * 100
        print(f"{ten:28s} : {cps_kb:8,.0f} đ | {diff:+6.1f}%")

    print('\n=== B2 · ĐỔI MỘT CẶP ===')
    res_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)
    print(f"Token x2 + Xem lại x2: {res_cap['cps']:,.0f} đ ({(res_cap['cps']/goc - 1)*100:+.1f}%)")

    print('\n=== B3 · GIỚI HẠN CHẠY LẠI & TOÀN HỆ THỐNG ===')
    for limit in [1, 2, 3]:
        kw = dict(max_lan_chay=limit) if limit < 3 else dict()
        res_lim = mo_hinh(runs, reqs, **kw)
        ko_thanh_cong = len(reqs) - res_lim['thanh_cong']
        chi_phi_he_thong = res_lim['tong'] + ko_thanh_cong * BASELINE
        print(f"Giới hạn {limit} lần | Tổng agent: {res_lim['tong']:10,.0f} đ | Không TC: {ko_thanh_cong:3d} | Cả hệ thống: {chi_phi_he_thong:10,.0f} đ | CPS: {res_lim['cps']:,.0f} đ")

    print('\n=== B4 · NẾU XEM LẠI 100% (noi_dia + hang_nang) ===')
    reqs_dn = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])].copy()
    runs_dn = runs[runs['request_id'].isin(reqs_dn['request_id'])].copy()
    # 1. Đếm yêu cầu có ít nhất 1 lần chạy ok
    reqs_with_ok = runs_dn[runs_dn['status'] == 'ok']['request_id'].unique()
    so_yc_ok = len(reqs_with_ok)
    tien_xem_lai_100 = so_yc_ok * 5 * LUONG_PHUT
    # 2. Đếm ca làm lại trong nhóm noi_dia + hang_nang (phut_lam_lai > 0)
    ca_lam_lai_dn = reqs_dn[reqs_dn['phut_lam_lai_simulated'] > 0]
    so_ca_lam_lai = len(ca_lam_lai_dn)
    tien_lam_lai_9m = so_ca_lam_lai * 9 * LUONG_PHUT
    tb_phut_lam_lai = ca_lam_lai_dn['phut_lam_lai_simulated'].mean()
    tien_lam_lai_real = ca_lam_lai_dn['phut_lam_lai_simulated'].sum() * LUONG_PHUT
    # 3. Token + tool
    tien_token_tool_dn = (runs_dn['tokens_in']/1000*26 + runs_dn['tokens_out']/1000*130 + runs_dn['tool_calls']*15).sum()
    # 4. Tổng và chia 900
    thanh_cong_dn = (reqs_dn['ket_qua'] == 'thanh_cong').sum()
    tong_9m = tien_token_tool_dn + tien_xem_lai_100 + tien_lam_lai_9m
    cps_9m = tong_9m / thanh_cong_dn
    tong_real = tien_token_tool_dn + tien_xem_lai_100 + tien_lam_lai_real
    cps_real = tong_real / thanh_cong_dn
    print(f"Số YC có chạy ok: {so_yc_ok} (tiền xem lại 5p: {tien_xem_lai_100:,.0f} đ)")
    print(f"Số ca làm lại: {so_ca_lam_lai} | Tiền làm lại 9p: {tien_lam_lai_9m:,.0f} đ | Tiền làm lại thực tế ({tb_phut_lam_lai:.1f}p): {tien_lam_lai_real:,.0f} đ")
    print(f"Tiền token+tool: {tien_token_tool_dn:,.0f} đ | Việc thành công: {thanh_cong_dn}")
    print(f"-> Giả định 9p: CPS = {cps_9m:,.0f} đ ({cps_9m/BASELINE:.2f}x)")
    print(f"-> Thực tế {tb_phut_lam_lai:.1f}p: CPS = {cps_real:,.0f} đ ({cps_real/BASELINE:.2f}x)")

    print('\n=== D1 · TÍNH CỠ MẪU ===')
    n_yc = tinh_co_mau(0.70, 0.75)
    print(f"a) Theo yêu cầu (0.70 -> 0.75): {n_yc} mỗi nhóm")
    de_b = 1 + (75 - 1) * 0.02
    n_b = math.ceil(n_yc * de_b)
    print(f"b) Theo nhân viên m=75 (DE={de_b:.2f}): {n_b} mỗi nhóm -> {n_b/75:.1f} người/nhóm")
    print(f"c) 20 nhân viên mỗi nhóm: Giới hạn c/ICC = 20/0.02 = {20/0.02:.0f} < {n_yc} (Không đạt)")
    print(f"d) 6 depot mỗi nhóm: Giới hạn 6/0.02 = {6/0.02:.0f} (Không đạt)")
    n_6pt = tinh_co_mau(0.70, 0.76)
    print(f"e) Mức chênh 6 điểm: n = {n_6pt} mỗi nhóm")
    # 20m / (1 + (m-1)*0.02) >= n_6pt => 20m >= n_6pt*(0.98 + 0.02m) => m*(20 - 0.02*n_6pt) >= 0.98*n_6pt
    m_req = (0.98 * n_6pt) / (20 - 0.02 * n_6pt)
    de_e = 1 + (math.ceil(m_req) - 1) * 0.02
    print(f"   m >= {m_req:.1f} -> m = {math.ceil(m_req)} YC/người | DE = {de_e:.2f}")

    # Power ở mức 5 điểm nếu chọn n_per_arm = n_6pt
    eff_size_5pt = 0.05 / math.sqrt(0.70 * 0.30)  # hoặc xấp xỉ
    power_5pt = NormalIndPower().power(effect_size=eff_size_5pt, nobs1=n_6pt, alpha=0.05, ratio=1.0)
    print(f"   Power ở mức 5 điểm với n={n_6pt}: {power_5pt:.2f}")
