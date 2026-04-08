class HangHoa:
    def __init__(self, ma_hang="", ten_hang="", nha_sx="", gia=0.0):
        self._ma_hang = ma_hang
        self._ten_hang = ten_hang
        self._nha_sx = nha_sx
        self._gia = gia

    def in_ttin(self):
        print(f"Ma hang: {self._ma_hang} | Ten: {self._ten_hang}")
        print(f"NSX: {self._nha_sx} | Gia: {self._gia:,.0f} VND")

class HangDienMay(HangHoa):
    def __init__(self, ma_hang="", ten_hang="", nha_sx="", gia=0.0, 
                 tg_baohanh=0, dien_ap=0, cong_suat=0):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__tg_baohanh = tg_baohanh
        self.__dien_ap = dien_ap
        self.__cong_suat = cong_suat

    def in_ttin(self):
        super().in_ttin()
        print(f"Bao hanh: {self.__tg_baohanh} thang | {self.__dien_ap}V - {self.__cong_suat}W")

class HangSanhSu(HangHoa):
    def __init__(self, ma_hang="", ten_hang="", nha_sx="", gia=0.0, loai_nguyenlieu=""):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__loai_nguyenlieu = loai_nguyenlieu

    def in_ttin(self):
        super().in_ttin()
        print(f"Nguyen lieu: {self.__loai_nguyenlieu}")

class HangThucPham(HangHoa):
    def __init__(self, ma_hang="", ten_hang="", nha_sx="", gia=0.0, ngay_sx="", ngay_hethan=""):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__ngay_sx = ngay_sx
        self.__ngay_hethan = ngay_hethan

    def in_ttin(self):
        super().in_ttin()
        print(f"NSX: {self.__ngay_sx} | HSD: {self.__ngay_hethan}")
