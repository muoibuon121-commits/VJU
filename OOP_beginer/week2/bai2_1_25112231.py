import math
def the_tich_cau():
    print("\n--- 2.1: Tính thể tích hình cầu ---")
    r = float(input("Nhập bán kính r: "))
    v = (4/3) * math.pi * (r**3)
    print(f"Thể tích hình cầu: {v:.2f}")

the_tich_cau()
