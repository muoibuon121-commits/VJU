import time
def thoi_gian_he_thong():
    print("\n--- 5.1: Xem thời gian từ Epoch ---")
    now = time.time()
    
    phut_s = 60
    gio_s = 3600
    ngay_s = 86400
    
    so_ngay = int(now // ngay_s)
    con_lai = now % ngay_s
    
    hh = int(con_lai // gio_s)
    con_lai %= gio_s
    mm = int(con_lai // phut_s)
    ss = int(con_lai % phut_s)
    
    print(f"Số ngày từ Epoch: {so_ngay}")
    print(f"Giờ GMT: {hh:02d}:{mm:02d}:{ss:02d}")
    print(f"Giờ Việt Nam (GMT+7): {(hh + 7) % 24:02d}:{mm:02d}:{ss:02d}")

thoi_gian_he_thong()
