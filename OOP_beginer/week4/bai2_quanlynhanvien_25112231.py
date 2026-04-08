class NhanVien:
    LUONG_MAX = 360000000 
    
    def __init__(self, ten_nv="", luong_cb=0, he_so=0.0):
        self.__ten_nv = ten_nv
        self.__luong_cb = luong_cb
        self.__he_so = he_so

    def get_ten_nv(self): return self.__ten_nv
    def get_luong_cb(self): return self.__luong_cb
    def get_he_so(self): return self.__he_so
    def set_he_so(self, he_so): self.__he_so = he_so

    def tinh_luong(self):
        return self.__luong_cb * self.__he_so

    def in_ttin(self):
        print(f"--- Thông tin nhân viên ---")
        print(f"Tên: {self.__ten_nv}")
        print(f"Lương thực nhận: {self.tinh_luong():,.0f} VNĐ")

    def tang_luong(self):
        try:
            delta = float(input(f"Nhập hệ số tăng thêm cho {self.__ten_nv}: "))
            luong_moi = self.__luong_cb * (self.__he_so + delta)
            
            if luong_moi > self.LUONG_MAX:
                print("Lỗi: Tổng lương vượt mức cho phép!")
                return False
            else:
                self.__he_so += delta
                print(f"Thành công. Hệ số mới: {self.__he_so}")
                return True
        except ValueError:
            print("Lỗi: Giá trị nhập vào phải là số.")
            return False

if __name__ == "__main__":
    print("--- KIỂM TRA LỚP NHÂN VIÊN ---")
    nv_muoi = NhanVien("Muối", 8100000, 5.5)
    nv_muoi.in_ttin()
    
    if nv_muoi.tang_luong():
        nv_muoi.in_ttin()
