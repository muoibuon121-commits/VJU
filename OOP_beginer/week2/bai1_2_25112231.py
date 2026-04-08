def km_to_miles():
    print("\n--- 1.2: Đổi KM sang Miles ---")
    x = float(input("Nhập số kilometers: "))
    y = x / 1.61
    don_vi = "mile" if y == 1 else "miles"
    print(f"{x} km bằng {y:.2f} {don_vi}")

km_to_miles()
