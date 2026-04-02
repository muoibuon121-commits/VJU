import copy

class HangHoa:
    def __init__(self, ma_hang="", ten_hang="", nha_sx="", gia=0.0):
        self._ma_hang = ma_hang
        self._ten_hang = ten_hang
        self._nha_sx = nha_sx
        self._gia = gia

    def in_ttin(self):
        print(f"Mã: {self._ma_hang} | Tên: {self._ten_hang} | "
              f"NSX: {self._nha_sx} | Giá: {self._gia:,.0f} VNĐ")


class HangDienMay(HangHoa):
    def __init__(self, ma_hang="", ten_hang="", nha_sx="", gia=0.0,
                 tg_baohanh=0, dien_ap=0, cong_suat=0):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__tg_baohanh = tg_baohanh
        self.__dien_ap = dien_ap
        self.__cong_suat = cong_suat

    def in_ttin(self):
        super().in_ttin()
        print(f"  -> Bảo hành: {self.__tg_baohanh} tháng | "
              f"{self.__dien_ap}V - {self.__cong_suat}W")


class HangSanhSu(HangHoa):
    def __init__(self, ma_hang="", ten_hang="", nha_sx="", gia=0.0,
                 loai_nguyenlieu=""):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__loai_nguyenlieu = loai_nguyenlieu

    def in_ttin(self):
        super().in_ttin()
        print(f"  -> Nguyên liệu: {self.__loai_nguyenlieu}")


class HangThucPham(HangHoa):
    def __init__(self, ma_hang="", ten_hang="", nha_sx="", gia=0.0,
                 ngay_sx="", ngay_hethan=""):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__ngay_sx = ngay_sx
        self.__ngay_hethan = ngay_hethan

    def in_ttin(self):
        super().in_ttin()
        print(f"  -> Ngày SX: {self.__ngay_sx} | HSD: {self.__ngay_hethan}")


class QLHangHoa:
    def __init__(self):
        self.danh_sach = []

    def them_hang(self, hang):
        self.danh_sach.append(hang)
        print("Thêm hàng hóa thành công!")

    def hien_thi(self):
        if not self.danh_sach:
            print("Danh sách hàng hóa đang trống.")
            return
        print("Danh sách hàng hóa:")
        for h in self.danh_sach:
            h.in_ttin()
            print("-" * 40)

    def tim_kiem(self, ten_tim):
        tu_khoa = ten_tim.strip().lower()
        ket_qua = [h for h in self.danh_sach if tu_khoa in h._ten_hang.lower()]
        if ket_qua:
            print(f'Kết quả tìm kiếm "{ten_tim}":')
            for h in ket_qua:
                h.in_ttin()
                print("-" * 40)
        else:
            print("Không tìm thấy hàng hóa phù hợp.")


class CanBo:
    def __init__(self, hoten="", tuoi=0, gioitinh="", diachi=""):
        self.__hoten = hoten
        self.__tuoi = tuoi
        self.__gioitinh = gioitinh
        self.__diachi = diachi

    def get_hoten(self):
        return self.__hoten

    def inTTin(self):
        print("Thông tin cán bộ:")
        print(f"  Họ và tên : {self.__hoten} | {self.__gioitinh} | {self.__tuoi} tuổi")
        print(f"  Địa chỉ   : {self.__diachi}")


class CongNhan(CanBo):
    def __init__(self, hoten="", tuoi=0, gioitinh="", diachi="", bac=0):
        super().__init__(hoten, tuoi, gioitinh, diachi)
        if 1 <= bac <= 10:
            self.__bac = bac
        else:
            self.__bac = 0
            print("Lỗi: Bậc công nhân phải từ 1 đến 10!")

    def inTTin(self):
        super().inTTin()
        print(f"  Bậc công nhân: {self.__bac}")


class KySu(CanBo):
    def __init__(self, hoten="", tuoi=0, gioitinh="", diachi="",
                 nganhdaotao=""):
        super().__init__(hoten, tuoi, gioitinh, diachi)
        self.__nganhdaotao = nganhdaotao

    def inTTin(self):
        super().inTTin()
        print(f"  Ngành đào tạo: {self.__nganhdaotao}")


class NhanVien(CanBo):
    def __init__(self, hoten="", tuoi=0, gioitinh="", diachi="",
                 congviec=""):
        super().__init__(hoten, tuoi, gioitinh, diachi)
        self.__congviec = congviec

    def inTTin(self):
        super().inTTin()
        print(f"  Công việc: {self.__congviec}")


class QLCB:
    def __init__(self):
        self.danhsach = []

    def addCB(self, canbo):
        self.danhsach.append(canbo)
        print("Thêm cán bộ thành công!")

    def timKiem(self, ten_tim_kiem):
        tu_khoa = ten_tim_kiem.strip().lower()
        ket_qua = [cb for cb in self.danhsach
                   if tu_khoa in cb.get_hoten().lower()]
        print(f'Kết quả tìm kiếm cho "{ten_tim_kiem}":')
        if ket_qua:
            for cb in ket_qua:
                cb.inTTin()
                print("-" * 25)
        else:
            print("Không tìm thấy cán bộ khớp tên này.")

    def hienthids(self):
        if not self.danhsach:
            print("Danh sách hiện đang trống.")
            return
        print("Danh sách cán bộ:")
        for cb in self.danhsach:
            cb.inTTin()
            print("-" * 25)


def menu_hang_hoa(ql_hh):
    while True:
        print("\n" + "-" * 35)
        print("  QUẢN LÝ HÀNG HÓA")
        print("-" * 35)
        print("1. Thêm hàng hóa mới")
        print("2. Tìm kiếm hàng hóa")
        print("3. Hiển thị danh sách")
        print("0. Quay lại menu chính")
        choice = input("Lựa chọn: ").strip()

        if choice == '1':
            print("\n-- Chọn loại hàng hóa --")
            print("1. Hàng điện máy | 2. Hàng sành sứ | 3. Hàng thực phẩm")
            loai = input("Lựa chọn: ").strip()
            if loai not in ['1', '2', '3']:
                print("Lựa chọn không hợp lệ!")
                continue
            ma = input("Mã hàng: ")
            ten = input("Tên hàng: ")
            nsx = input("Nhà sản xuất: ")
            gia = float(input("Giá (VNĐ): "))
            if loai == '1':
                bh = int(input("Thời gian bảo hành (tháng): "))
                dap = int(input("Điện áp (V): "))
                cs = int(input("Công suất (W): "))
                ql_hh.them_hang(HangDienMay(ma, ten, nsx, gia, bh, dap, cs))
            elif loai == '2':
                nl = input("Loại nguyên liệu: ")
                ql_hh.them_hang(HangSanhSu(ma, ten, nsx, gia, nl))
            elif loai == '3':
                ngay_sx = input("Ngày sản xuất (dd/mm/yyyy): ")
                hsd = input("Hạn sử dụng (dd/mm/yyyy): ")
                ql_hh.them_hang(HangThucPham(ma, ten, nsx, gia, ngay_sx, hsd))

        elif choice == '2':
            ten = input("Nhập tên hàng cần tìm: ")
            ql_hh.tim_kiem(ten)

        elif choice == '3':
            ql_hh.hien_thi()

        elif choice == '0':
            break
        else:
            print("Vui lòng nhập lại!")


def menu_can_bo(ql_cb):
    while True:
        print("\n" + "-" * 35)
        print("  QUẢN LÝ CÁN BỘ")
        print("-" * 35)
        print("1. Thêm mới cán bộ")
        print("2. Tìm kiếm theo họ tên")
        print("3. Hiển thị danh sách")
        print("0. Quay lại menu chính")
        choice = input("Lựa chọn: ").strip()

        if choice == '1':
            print("\n-- Chọn loại cán bộ --")
            print("1. Công nhân | 2. Kỹ sư | 3. Nhân viên")
            loai = input("Lựa chọn: ").strip()
            if loai not in ['1', '2', '3']:
                print("Lựa chọn không hợp lệ!")
                continue
            hoten = input("Họ và tên: ")
            tuoi = int(input("Tuổi: "))
            gioitinh = input("Giới tính: ")
            diachi = input("Địa chỉ: ")
            if loai == '1':
                bac = int(input("Bậc công nhân (1-10): "))
                ql_cb.addCB(CongNhan(hoten, tuoi, gioitinh, diachi, bac))
            elif loai == '2':
                nganh = input("Ngành đào tạo: ")
                ql_cb.addCB(KySu(hoten, tuoi, gioitinh, diachi, nganh))
            elif loai == '3':
                viec = input("Công việc: ")
                ql_cb.addCB(NhanVien(hoten, tuoi, gioitinh, diachi, viec))

        elif choice == '2':
            ten = input("Nhập tên cán bộ cần tìm: ")
            ql_cb.timKiem(ten)

        elif choice == '3':
            ql_cb.hienthids()

        elif choice == '0':
            break
        else:
            print("Vui lòng nhập lại!")


def main():
    ql_hh = QLHangHoa()
    ql_cb = QLCB()

    while True:
        print("\n" + "=" * 35)
        print("   CHƯƠNG TRÌNH QUẢN LÝ TỔNG HỢP")
        print("=" * 35)
        print("1. Quản lý Hàng Hóa")
        print("2. Quản lý Cán Bộ")
        print("3. Thoát")
        choice = input("Lựa chọn: ").strip()

        if choice == '1':
            menu_hang_hoa(ql_hh)
        elif choice == '2':
            menu_can_bo(ql_cb)
        elif choice == '3':
            print("Thoát chương trình. Tạm biệt!")
            break
        else:
            print("Vui lòng nhập lại!")


if __name__ == "__main__":
    main()
