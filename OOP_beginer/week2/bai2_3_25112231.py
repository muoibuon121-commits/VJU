def thoi_gian_ve_nha():
    print("\n--- 2.3: Tính giờ về ăn sáng ---")
    h_start = int(input("Giờ xuất phát: "))
    m_start = int(input("Phút xuất phát: "))
    
    # Pace quy đổi ra giây
    pace_easy = 8 * 60 + 15
    pace_mid = 7 * 60 + 12
    
    d1 = float(input("Số dặm chạy dễ 1: "))
    d2 = float(input("Số dặm chạy nhanh: "))
    d3 = float(input("Số dặm chạy dễ 2: "))
    
    tong_giay_chay = d1*pace_easy + d2*pace_mid + d3*pace_easy
    tong_giay_start = h_start * 3600 + m_start * 60
    tong_giay_cuoi = tong_giay_start + tong_giay_chay
    
    h_end = int(tong_giay_cuoi // 3600 % 24)
    m_end = int(tong_giay_cuoi % 3600 // 60)
    s_end = int(tong_giay_cuoi % 60)
    
    print(f"Bạn về ăn sáng lúc: {h_end:02d}:{m_end:02d}:{s_end:02d}")

thoi_gian_ve_nha()
