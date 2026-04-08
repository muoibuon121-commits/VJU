class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten 
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def __str__(self):
        return f"Gao {self.ten} | Vũ khí: {self.vu_khi} | Màu: {self.mau_sac}"

if __name__ == '__main__':
    team = []
    n = int(input("Số lượng siêu nhân: "))
    for i in range(n):
        print(f"Nhập Gao thứ {i+1}:")
        s = SieuNhan(input("Tên: "), input("Vũ khí: "), input("Màu: "))
        team.append(s)
    
    print("\n--- DANH SÁCH TEAM GAO ---")
    for s in team:
        print(s)
