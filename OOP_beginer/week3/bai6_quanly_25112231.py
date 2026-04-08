class NhanVien:
    LUONG_MAX = 50_000_000

    def __init__(self, ten, luong_cb, he_so):
        self.ten = ten
        self.luong_cb = luong_cb
        self.he_so = he_so

    def tinh_luong(self):
        return self.luong_cb * self.he_so

    def tang_luong(self, delta):
        luong_moi = self.luong_cb * (self.he_so + delta)
        if luong_moi > NhanVien.LUONG_MAX:
            print(" Lương quá cao, sếp không duyệt!")
            return False
        self.he_so += delta
        print(" Tăng lương thành công!")
        return True

if __name__ == '__main__':
    nv = NhanVien("Trần Muối", 10_000_000, 1.5)
    print(f"Lương hiện tại: {nv.tinh_luong():,.0f}")
    nv.tang_luong(3.0)
