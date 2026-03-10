
# 2.1 Giá 1 cuốn sách là 24.95$, nhưng được giảm giá 40%, phí vận chuyển là 3$ cho 1 cuốn đầu và các cuốn sau là 75 cents -> nhập số sách cần mua
sach = (input("Nhập số sách cần mua:"))
if sach.isdigit():
    S = int(sach)
    if S >= 1:
        print(f"Tổng số tiền là:{(S*24.95*0.6)+ 3 + ((S-1)*0.75):.2f} Đô")
    else: 
        print("Em không bán sách nửa cuốn sách anh ạ!")
else:
    print("Em không bán nửa cuốn đâu !")