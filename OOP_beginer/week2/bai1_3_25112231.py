def tinh_toc_do():
    print("\n--- 1.3: Tính tốc độ chạy ---")
    km = float(input("Nhập số KM đã chạy: "))
    m = float(input("Nhập số phút đã chạy: "))
    n = float(input("Nhập số giây đã chạy: "))
    
    quang_duong_mile = km / 1.61
    tong_giay = m * 60 + n
    tong_gio = tong_giay / 3600
    
    pace = (m + n/60) / quang_duong_mile
    speed_mph = quang_duong_mile / tong_gio
    
    print(f"PACE: {pace:.2f} mile/minutes")
    print(f"Tốc độ trung bình: {speed_mph:.2f} mile/hours")

tinh_toc_do()
