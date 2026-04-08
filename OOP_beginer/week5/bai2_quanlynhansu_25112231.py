class NhanVienBase:
    def __init__(self, ma_nv="", ho_ten="", nam_sinh=0, gioi_tinh="", diachi="", he_so=0.0, luong_max=0.0):
        self._ma_nv = ma_nv
        self._ho_ten = ho_ten
        self._nam_sinh = nam_sinh
        self._gioi_tinh = gioi_tinh
        self._diachi = diachi
        self._he_so = he_so if he_so > 0 else 1.0
        self._luong_max = luong_max

    def in_ttin(self):
        print(f"Ma NV: {self._ma_nv} | Ho ten: {self._ho_ten} | He so: {self._he_so}")

class CongTacVien(NhanVienBase):
    def __init__(self, **kwargs):
        # kwargs chua thong tin chung va thong tin rieng cua CTV
        super().__init__(kwargs.get('ma_nv'), kwargs.get('ho_ten'), kwargs.get('nam_sinh'),
                         kwargs.get('gioi_tinh'), kwargs.get('diachi'), kwargs.get('he_so'), kwargs.get('luong_max'))
        self.__thoi_han = kwargs.get('thoi_han') # 3 thang, 6 thang, 1 nam
        self.__phu_cap_ld = kwargs.get('phu_cap_ld', 0.0)

    def in_ttin(self):
        super().in_ttin()
        print(f"Loai: Cong tac vien | Thoi han: {self.__thoi_han} | Phu cap: {self.__phu_cap_ld:,.0f}")

class TruongPhong(NhanVienBase):
    def __init__(self, **kwargs):
        super().__init__(kwargs.get('ma_nv'), kwargs.get('ho_ten'), kwargs.get('nam_sinh'),
                         kwargs.get('gioi_tinh'), kwargs.get('diachi'), kwargs.get('he_so'), kwargs.get('luong_max'))
        self.__ngay_quan_ly = kwargs.get('ngay_quan_ly')
        self.__phu_cap_ql = kwargs.get('phu_cap_ql', 0.0)

    def in_ttin(self):
        super().in_ttin()
        print(f"Chuc vu: Truong phong | Ngay bat dau QL: {self.__ngay_quan_ly} | Phu cap QL: {self.__phu_cap_ql:,.0f}")
