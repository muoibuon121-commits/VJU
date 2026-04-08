def ve_luoi_linh_hoat():
    print("\n--- 3.1 & 3.2: Vẽ lưới n hàng n cột ---")
    hang = int(input("Nhập số hàng: "))
    cot = int(input("Nhập số cột: "))
    
    s_line = '+' + '-'*4
    s_block = '|' + ' '*4
    
    def ve_mot_tang():
        # Vẽ dòng kẻ ngang
        print(s_line * cot + '+')
        # Vẽ 4 dòng kẻ dọc
        for _ in range(4):
            print(s_block * cot + '|')

    for _ in range(hang):
        ve_mot_tang()
    print(s_line * cot + '+') # Dòng chốt cuối

ve_luoi_linh_hoat()
