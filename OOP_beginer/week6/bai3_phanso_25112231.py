from math import gcd

class MauSoBangKhong(Exception):
    pass

class PhanSo:
    def __init__(self, tu, mau):
        if mau == 0:
            raise MauSoBangKhong('Mẫu số không được bằng 0')
        
        d = gcd(abs(tu), abs(mau))
        self._tu = tu // d
        self._mau = mau // d
        
        if self._mau < 0:
            self._tu = -self._tu
            self._mau = -self._mau
    
    @property
    def tu(self):
        return self._tu
    
    @property
    def mau(self):
        return self._mau
    
    def la_toi_gian(self):
        return gcd(abs(self._tu), abs(self._mau)) == 1
    
    def toi_gian(self):
        d = gcd(abs(self._tu), abs(self._mau))
        return PhanSo(self._tu // d, self._mau // d)
    
    def __str__(self):
        if self._mau == 1:
            return str(self._tu)
        return f'{self._tu}/{self._mau}'
    
    def __repr__(self):
        return f'PhanSo({self._tu}, {self._mau})'
    
    def __add__(self, other):
        if not isinstance(other, PhanSo):
            raise TypeError('Chỉ có thể cộng với PhanSo')
        tu = self._tu * other._mau + other._tu * self._mau
        mau = self._mau * other._mau
        return PhanSo(tu, mau)
    
    def __sub__(self, other):
        if not isinstance(other, PhanSo):
            raise TypeError('Chỉ có thể trừ với PhanSo')
        tu = self._tu * other._mau - other._tu * self._mau
        mau = self._mau * other._mau
        return PhanSo(tu, mau)
    
    def __mul__(self, other):
        if not isinstance(other, PhanSo):
            raise TypeError('Chỉ có thể nhân với PhanSo')
        tu = self._tu * other._tu
        mau = self._mau * other._mau
        return PhanSo(tu, mau)
    
    def __truediv__(self, other):
        if not isinstance(other, PhanSo):
            raise TypeError('Chỉ có thể chia với PhanSo')
        if other._tu == 0:
            raise ValueError('Không thể chia cho phân số có tử = 0')
        tu = self._tu * other._mau
        mau = self._mau * other._tu
        return PhanSo(tu, mau)
    
    def __eq__(self, other):
        if not isinstance(other, PhanSo):
            return False
        return self._tu * other._mau == other._tu * self._mau
    
    def __lt__(self, other):
        if not isinstance(other, PhanSo):
            raise TypeError('Chỉ có thể so sánh với PhanSo')
        return self._tu * other._mau < other._tu * self._mau
    
    def __le__(self, other):
        return self < other or self == other
    
    def __gt__(self, other):
        if not isinstance(other, PhanSo):
            raise TypeError('Chỉ có thể so sánh với PhanSo')
        return self._tu * other._mau > other._tu * self._mau
    
    def __ge__(self, other):
        return self > other or self == other
    
    def __hash__(self):
        return hash((self._tu, self._mau))
