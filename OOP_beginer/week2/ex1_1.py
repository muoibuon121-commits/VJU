def tinh_giay():
    print("--- 1.1: Đổi phút giây sang giây ---")
    m = float(input("Nhập số phút: "))
    n = int(input("Nhập số giây: "))
    tong_giay = m * 60 + n
    print(f"Tổng cộng: {tong_giay} giây")

tinh_giay()
