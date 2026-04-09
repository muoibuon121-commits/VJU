from abc import ABC, abstractmethod

class TuoiKhongHopLe(Exception):
    pass

class BacKhongHopLe(Exception):
    pass

class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        if not (18 <= tuoi <= 65):
            raise TuoiKhongHopLe('Tuổi phải từ 18 đến 65')
        self._ho_ten = ho_ten
        self._tuoi = tuoi
        self._gioi_tinh = gioi_tinh
        self._dia_chi = dia_chi
    
    @property
    def ho_ten(self):
        return self._ho_ten
    
    @property
    def tuoi(self):
        return self._tuoi
    
    @tuoi.setter
    def tuoi(self, value):
        if not (18 <= value <= 65):
            raise TuoiKhongHopLe('Tuổi phải từ 18 đến 65')
        self._tuoi = value
    
    @property
    def gioi_tinh(self):
        return self._gioi_tinh
    
    @property
    def dia_chi(self):
        return self._dia_chi
    
    @abstractmethod
    def mo_ta(self):
        pass
    
    def __str__(self):
        return f'{self._ho_ten} ({self._tuoi}), {self._gioi_tinh}, {self._dia_chi}'
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self._ho_ten}, {self._tuoi})'
    
    def __eq__(self, other):
        if not isinstance(other, CanBo):
            return False
        return self._ho_ten == other._ho_ten and self._tuoi == other._tuoi
    
    def __lt__(self, other):
        return self._ho_ten < other._ho_ten

class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        if not (1 <= bac <= 10):
            raise BacKhongHopLe('Bậc phải từ 1 đến 10')
        self._bac = bac
    
    @property
    def bac(self):
        return self._bac
    
    @bac.setter
    def bac(self, value):
        if not (1 <= value <= 10):
            raise BacKhongHopLe('Bậc phải từ 1 đến 10')
        self._bac = value
    
    def mo_ta(self):
        return f'Công nhân {self._ho_ten} (Bậc {self._bac})'

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self._nganh_dao_tao = nganh_dao_tao
    
    @property
    def nganh_dao_tao(self):
        return self._nganh_dao_tao
    
    @nganh_dao_tao.setter
    def nganh_dao_tao(self, value):
        if not value:
            raise ValueError('Ngành đào tạo không được rỗng')
        self._nganh_dao_tao = value
    
    def mo_ta(self):
        return f'Kỹ sư {self._ho_ten} ({self._nganh_dao_tao})'

class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self._cong_viec = cong_viec
    
    @property
    def cong_viec(self):
        return self._cong_viec
    
    @cong_viec.setter
    def cong_viec(self, value):
        if not value:
            raise ValueError('Công việc không được rỗng')
        self._cong_viec = value
    
    def mo_ta(self):
        return f'Nhân viên {self._ho_ten} ({self._cong_viec})'

class QuanLyCanBo:
    def __init__(self, file_path):
        self.file_path = file_path
        self.can_bo = []
    
    def them_can_bo(self, cb):
        self.can_bo.append(cb)
    
    def sap_xep_theo_ten(self):
        return sorted(self.can_bo)
    
    def dem_theo_loai(self):
        counts = {
            'CongNhan': 0,
            'KySu': 0,
            'NhanVien': 0
        }
        for cb in self.can_bo:
            if isinstance(cb, CongNhan):
                counts['CongNhan'] += 1
            elif isinstance(cb, KySu):
                counts['KySu'] += 1
            elif isinstance(cb, NhanVien):
                counts['NhanVien'] += 1
        return counts
    
    def luu_file(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            for cb in self.can_bo:
                f.write(f'{cb} → {cb.mo_ta()}\n')
    
    def doc_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            print(f.read())

if __name__ == '__main__':
    ql = QuanLyCanBo('canbo.txt')
    
    cn1 = CongNhan('Trần Ngô Tiến Đạt', 19, 'Nam', 'Thừa Thiên Huế', 5)
    cn2 = CongNhan('Phạm Hồng Duyên', 18, 'Nữ', 'Nam Định', 3)
    ks1 = KySu('Lê Văn C', 40, 'Nam', 'Đà Nẵng', 'CNTT')
    ks2 = KySu('Phạm Thị D', 32, 'Nữ', 'Hải Phòng', 'Xây dựng')
    nv1 = NhanVien('Hoàng Văn E', 25, 'Nam', 'Cần Thơ', 'Kinh doanh')
    
    ql.them_can_bo(cn1)
    ql.them_can_bo(cn2)
    ql.them_can_bo(ks1)
    ql.them_can_bo(ks2)
    ql.them_can_bo(nv1)
    
    print('Danh sách theo tên (A→Z)')
    for cb in ql.sap_xep_theo_ten():
        print(f'{cb} → {cb.mo_ta()}')
    
    print('\nThống kê theo loại')
    counts = ql.dem_theo_loai()
    print(f'Công nhân: {counts["CongNhan"]}')
    print(f'Kỹ sư: {counts["KySu"]}')
    print(f'Nhân viên: {counts["NhanVien"]}')
    
    ql.luu_file()
    print('\nDữ liệu đã lưu vào file')
    ql.doc_file()
