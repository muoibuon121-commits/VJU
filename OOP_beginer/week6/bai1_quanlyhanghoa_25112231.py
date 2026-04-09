from abc import ABC, abstractmethod
from datetime import datetime

class MauSoKhongHopLe(Exception):
    pass

class HangHoa(ABC):
    def __init__(self, ma, ten, gia):
        if gia <= 0:
            raise MauSoKhongHopLe('Giá phải > 0')
        self._ma = ma
        self._ten = ten
        self._gia = gia
    
    @property
    def ma(self):
        return self._ma
    
    @property
    def ten(self):
        return self._ten
    
    @ten.setter
    def ten(self, value):
        if not value:
            raise ValueError('Tên không được rỗng')
        self._ten = value
    
    @property
    def gia(self):
        return self._gia
    
    @gia.setter
    def gia(self, value):
        if value <= 0:
            raise MauSoKhongHopLe('Giá phải > 0')
        self._gia = value
    
    @abstractmethod
    def inTTin(self):
        pass
    
    def __str__(self):
        return f'[{self._ma}] {self._ten}: {self._gia:,.0f}đ'
    
    def __repr__(self):
        return f'HangHoa(ma={self._ma}, ten={self._ten}, gia={self._gia})'
    
    def __eq__(self, other):
        if not isinstance(other, HangHoa):
            return False
        return self._ma == other._ma
    
    def __lt__(self, other):
        return self._gia < other._gia
    
    def __hash__(self):
        return hash(self._ma)

class HangHoaDienTu(HangHoa):
    def __init__(self, ma, ten, gia, thoi_han_bao_hanh):
        super().__init__(ma, ten, gia)
        self._thoi_han_bao_hanh = thoi_han_bao_hanh
    
    @property
    def thoi_han_bao_hanh(self):
        return self._thoi_han_bao_hanh
    
    @thoi_han_bao_hanh.setter
    def thoi_han_bao_hanh(self, value):
        if value <= 0:
            raise ValueError('Thời hạn phải > 0')
        self._thoi_han_bao_hanh = value
    
    def inTTin(self):
        return f'Điện tử: {self._ten}, BH: {self._thoi_han_bao_hanh} tháng'

class HangHoaSanh(HangHoa):
    def __init__(self, ma, ten, gia, chat_lieu):
        super().__init__(ma, ten, gia)
        self._chat_lieu = chat_lieu
    
    @property
    def chat_lieu(self):
        return self._chat_lieu
    
    @chat_lieu.setter
    def chat_lieu(self, value):
        if not value:
            raise ValueError('Chất liệu không được rỗng')
        self._chat_lieu = value
    
    def inTTin(self):
        return f'Sành: {self._ten}, {self._chat_lieu}'

class HangHoaThucPham(HangHoa):
    def __init__(self, ma, ten, gia, han_su_dung):
        super().__init__(ma, ten, gia)
        self._han_su_dung = han_su_dung
    
    @property
    def han_su_dung(self):
        return self._han_su_dung
    
    @han_su_dung.setter
    def han_su_dung(self, value):
        han = datetime.strptime(value, '%Y-%m-%d')
        if han <= datetime.now():
            raise ValueError('Hạn sử dụng phải sau ngày hôm nay')
        self._han_su_dung = value
    
    def inTTin(self):
        return f'Thực phẩm: {self._ten}, HSD: {self._han_su_dung}'

class QuanLyHangHoa:
    def __init__(self, file_path):
        self.file_path = file_path
        self.hang_hoa = []
    
    def them_hang_hoa(self, hh):
        if any(h.ma == hh.ma for h in self.hang_hoa):
            raise ValueError(f'Mã {hh.ma} đã tồn tại')
        self.hang_hoa.append(hh)
    
    def xoa_hang_hoa(self, ma):
        self.hang_hoa = [h for h in self.hang_hoa if h.ma != ma]
    
    def tim_theo_gia(self, gia_min, gia_max):
        return [h for h in self.hang_hoa if gia_min <= h.gia <= gia_max]
    
    def sap_xep_theo_gia(self):
        return sorted(self.hang_hoa)
    
    def luu_file(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            for hh in self.hang_hoa:
                f.write(f'{hh}\n')
    
    def doc_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
    
    def __str__(self):
        return f'Quản lý {len(self.hang_hoa)} hàng hóa'

if __name__ == '__main__':
    ql = QuanLyHangHoa('hanghoa.txt')

    hh1 = HangHoaDienTu('DT001', 'Macbook Pro M4 16inch 2TB', 150000000, 24)
    hh2 = HangHoaSanh('SN001', 'Bình gốm', 500000, 'Gốm sứ Bát Tràng')
    hh3 = HangHoaThucPham('TP001', 'Sữa tươi', 10000, '2025-12-31')
    
    ql.them_hang_hoa(hh1)
    ql.them_hang_hoa(hh2)
    ql.them_hang_hoa(hh3)
    
    print('Tất cả hàng hóa')
    for hh in ql.hang_hoa:
        print(hh)

    print('\nSắp xếp theo giá (tăng dần)')
    for hh in ql.sap_xep_theo_gia():
        print(hh)
    
    ql.luu_file()
    print('\nDữ liệu đã lưu vào file')
    ql.doc_file()
