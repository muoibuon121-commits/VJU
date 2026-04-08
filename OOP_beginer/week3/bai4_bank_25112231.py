class BankAccount:
    def __init__(self, chu_tk, so_du):
        self.chu_tk = chu_tk
        self.so_du = so_du

    def giao_dich(self):
        print(f"\nTK: {self.chu_tk} | Số dư: {self.so_du:,.0f} VNĐ")
        opt = input("Bạn muốn (rút/gửi): ").lower()
        tien = float(input("Nhập số tiền: "))
        
        if opt == "rút":
            if tien > self.so_du:
                print("❌ Nghèo rồi, không đủ tiền rút!")
            else:
                self.so_du -= tien
                print(f"✅ Rút thành công. Còn lại: {self.so_du:,.0f}")
        elif opt == "gửi":
            self.so_du += tien
            print(f"✅ Đã gửi. Số dư mới: {self.so_du:,.0f}")

if __name__ == '__main__':
    acc = BankAccount("Trần Muối", 1000000)
    acc.giao_dich()
