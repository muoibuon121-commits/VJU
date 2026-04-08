def tinh_tien_sach():
    print("\n--- 2.2: Tính tiền mua sách ---")
    sach_input = input("Nhập số sách cần mua: ")
    if sach_input.isdigit():
        s = int(sach_input)
        if s >= 1:
            gia_giam = 24.95 * 0.6
            phi_ship = 3 + (s - 1) * 0.75
            tong = (s * gia_giam) + phi_ship
            print(f"Tổng số tiền: {tong:.2f} Đô")
        else:
            print("Số lượng không hợp lệ!")
    else:
        print("Vui lòng nhập số nguyên!")

tinh_tien_sach()
