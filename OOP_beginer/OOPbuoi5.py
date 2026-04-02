import copy

# ==========================================
# PHAN 1: QUAN LY HANG HOA
# ==========================================
class HangHoa:
    def __init__(self, ma_hang="", ten_hang="", nha_sx="", gia=0.0):
        self._ma_hang = ma_hang
        self._ten_hang = ten_hang
        self._nha_sx = nha_sx
        self._gia = gia

    def in_ttin(self):
        print(f"Ma: {self._ma_hang} | Ten: {self._ten_hang} | "
              f"NSX: {self._nha_sx} | Gia: {self._gia:,.0f} VND")


class HangDienMay(HangHoa):
    def __init__(self, ma_hang="", ten_hang="", nha_sx="", gia=0.0,
                 tg_baohanh=0, dien_ap=0, cong_suat=0):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__tg_baohanh = tg_baohanh
        self.__dien_ap = dien_ap
        self.__cong_suat = cong_suat

    def in_ttin(self):
        super().in_ttin()
        print(f"  -> Bao hanh: {self.__tg_baohanh} thang | "
              f"{self.__dien_ap}V - {self.__cong_suat}W")


class HangSanhSu(HangHoa):
    def __init__(self, ma_hang="", ten_hang="", nha_sx="", gia=0.0,
                 loai_nguyenlieu=""):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__loai_nguyenlieu = loai_nguyenlieu

    def in_ttin(self):
        super().in_ttin()
        print(f"  -> Nguyen lieu: {self.__loai_nguyenlieu}")


class HangThucPham(HangHoa):
    def __init__(self, ma_hang="", ten_hang="", nha_sx="", gia=0.0,
                 ngay_sx="", ngay_hethan=""):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__ngay_sx = ngay_sx
        self.__ngay_hethan = ngay_hethan

    def in_ttin(self):
        super().in_ttin()
        print(f"  -> Ngay SX: {self.__ngay_sx} | HSD: {self.__ngay_hethan}")


class QLHangHoa:
    def __init__(self):
        self.danh_sach = []

    def them_hang(self, hang):
        self.danh_sach.append(hang)
        print("Them hang hoa thanh cong!")

    def hien_thi(self):
        if not self.danh_sach:
            print("Danh sach hang hoa dang trong.")
            return
        print("Danh sach hang hoa:")
        for h in self.danh_sach:
            h.in_ttin()
            print("-" * 40)

    def tim_kiem(self, ten_tim):
        tu_khoa = ten_tim.strip().lower()
        ket_qua = [h for h in self.danh_sach if tu_khoa in h._ten_hang.lower()]
        if ket_qua:
            print(f'Ket qua tim kiem "{ten_tim}":')
            for h in ket_qua:
                h.in_ttin()
                print("-" * 40)
        else:
            print("Khong tim thay hang hoa phu hop.")


# ==========================================
# PHAN 2: QUAN LY CAN BO
# ==========================================
class CanBo:
    def __init__(self, hoten="", tuoi=0, gioitinh="", diachi=""):
        self.__hoten = hoten
        self.__tuoi = tuoi
        self.__gioitinh = gioitinh
        self.__diachi = diachi

    def get_hoten(self):
        return self.__hoten

    # Đổi inTTin -> inTTin() làm base, lớp con override thống nhất
    def inTTin(self):
        print("Thong tin can bo:")
        print(f"  Ho va ten : {self.__hoten} | {self.__gioitinh} | {self.__tuoi} tuoi")
        print(f"  Dia chi   : {self.__diachi}")


class CongNhan(CanBo):
    def __init__(self, hoten="", tuoi=0, gioitinh="", diachi="", bac=0):
        super().__init__(hoten, tuoi, gioitinh, diachi)
        if 1 <= bac <= 10:
            self.__bac = bac
        else:
            self.__bac = 0
            print("Loi: Bac cong nhan phai tu 1 den 10!")

    # Override inTTin() thay vi inTTin1() -> nhat quan
    def inTTin(self):
        super().inTTin()
        print(f"  Bac cong nhan: {self.__bac}")


class KySu(CanBo):
    def __init__(self, hoten="", tuoi=0, gioitinh="", diachi="",
                 nganhdaotao=""):
        super().__init__(hoten, tuoi, gioitinh, diachi)
        self.__nganhdaotao = nganhdaotao

    def inTTin(self):
        super().inTTin()
        print(f"  Nganh dao tao: {self.__nganhdaotao}")


class NhanVien(CanBo):
    def __init__(self, hoten="", tuoi=0, gioitinh="", diachi="",
                 congviec=""):
        super().__init__(hoten, tuoi, gioitinh, diachi)
        self.__congviec = congviec

    def inTTin(self):
        super().inTTin()
        print(f"  Cong viec: {self.__congviec}")


class QLCB:
    def __init__(self):
        self.danhsach = []

    def addCB(self, canbo):
        self.danhsach.append(canbo)
        print("Them can bo thanh cong!")

    def timKiem(self, ten_tim_kiem):
        tu_khoa = ten_tim_kiem.strip().lower()
        ket_qua = [cb for cb in self.danhsach
                   if tu_khoa in cb.get_hoten().lower()]
        print(f'Ket qua tim kiem cho "{ten_tim_kiem}":')
        if ket_qua:
            for cb in ket_qua:
                cb.inTTin()
                print("-" * 25)
        else:
            print("Khong tim thay can bo khop ten nay.")

    def hienthids(self):
        if not self.danhsach:
            print("Danh sach hien dang trong.")
            return
        print("Danh sach can bo:")
        for cb in self.danhsach:
            cb.inTTin()
            print("-" * 25)


# ==========================================
# MENU CHINH
# ==========================================
def menu_hang_hoa(ql_hh):
    while True:
        print("\n" + "-" * 35)
        print("  QUAN LY HANG HOA")
        print("-" * 35)
        print("1. Them hang hoa moi")
        print("2. Tim kiem hang hoa")
        print("3. Hien thi danh sach")
        print("0. Quay lai menu chinh")
        choice = input("Lua chon: ").strip()

        if choice == '1':
            print("\n-- Chon loai hang hoa --")
            print("1. Hang dien may | 2. Hang sanh su | 3. Hang thuc pham")
            loai = input("Lua chon: ").strip()
            if loai not in ['1', '2', '3']:
                print("Lua chon khong hop le!")
                continue
            ma = input("Ma hang: ")
            ten = input("Ten hang: ")
            nsx = input("Nha san xuat: ")
            gia = float(input("Gia (VND): "))
            if loai == '1':
                bh = int(input("Thoi gian bao hanh (thang): "))
                dap = int(input("Dien ap (V): "))
                cs = int(input("Cong suat (W): "))
                ql_hh.them_hang(HangDienMay(ma, ten, nsx, gia, bh, dap, cs))
            elif loai == '2':
                nl = input("Loai nguyen lieu: ")
                ql_hh.them_hang(HangSanhSu(ma, ten, nsx, gia, nl))
            elif loai == '3':
                ngay_sx = input("Ngay san xuat (dd/mm/yyyy): ")
                hsd = input("Han su dung (dd/mm/yyyy): ")
                ql_hh.them_hang(HangThucPham(ma, ten, nsx, gia, ngay_sx, hsd))

        elif choice == '2':
            ten = input("Nhap ten hang can tim: ")
            ql_hh.tim_kiem(ten)

        elif choice == '3':
            ql_hh.hien_thi()

        elif choice == '0':
            break
        else:
            print("Vui long nhap lai!")


def menu_can_bo(ql_cb):
    while True:
        print("\n" + "-" * 35)
        print("  QUAN LY CAN BO")
        print("-" * 35)
        print("1. Them moi can bo")
        print("2. Tim kiem theo ho ten")
        print("3. Hien thi danh sach")
        print("0. Quay lai menu chinh")
        choice = input("Lua chon: ").strip()

        if choice == '1':
            print("\n-- Chon loai can bo --")
            print("1. Cong nhan | 2. Ky su | 3. Nhan vien")
            loai = input("Lua chon: ").strip()
            if loai not in ['1', '2', '3']:
                print("Lua chon khong hop le!")
                continue
            hoten = input("Ho va ten: ")
            tuoi = int(input("Tuoi: "))
            gioitinh = input("Gioi tinh: ")
            diachi = input("Dia chi: ")
            if loai == '1':
                bac = int(input("Bac cong nhan (1-10): "))
                ql_cb.addCB(CongNhan(hoten, tuoi, gioitinh, diachi, bac))
            elif loai == '2':
                nganh = input("Nganh dao tao: ")
                ql_cb.addCB(KySu(hoten, tuoi, gioitinh, diachi, nganh))
            elif loai == '3':
                viec = input("Cong viec: ")
                ql_cb.addCB(NhanVien(hoten, tuoi, gioitinh, diachi, viec))

        elif choice == '2':
            ten = input("Nhap ten can bo can tim: ")
            ql_cb.timKiem(ten)

        elif choice == '3':
            ql_cb.hienthids()

        elif choice == '0':
            break
        else:
            print("Vui long nhap lai!")


def main():
    ql_hh = QLHangHoa()
    ql_cb = QLCB()

    while True:
        print("\n" + "=" * 35)
        print("   CHUONG TRINH QUAN LY TONG HOP")
        print("=" * 35)
        print("1. Quan ly Hang Hoa")
        print("2. Quan ly Can Bo")
        print("3. Thoat")
        choice = input("Lua chon: ").strip()

        if choice == '1':
            menu_hang_hoa(ql_hh)
        elif choice == '2':
            menu_can_bo(ql_cb)
        elif choice == '3':
            print("Thoat chuong trinh. Tam biet!")
            break
        else:
            print("Vui long nhap lai!")


if __name__ == "__main__":
    main()
