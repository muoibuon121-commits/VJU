class CanBo:
    def __init__(self, ho_ten="", tuoi=0, gioi_tinh="", dia_chi=""):
        self._ho_ten = ho_ten
        self._tuoi = tuoi
        self._gioi_tinh = gioi_tinh
        self._dia_chi = dia_chi

    def get_ho_ten(self):
        return self._ho_ten

class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__bac = bac if 1 <= bac <= 10 else 1

class QLCB:
    def __init__(self):
        self.danh_sach = []

    def them_moi(self, can_bo):
        self.danh_sach.append(can_bo)
        print("Da them can bo vao danh sach.")

    def tim_kiem_ten(self, ten):
        ket_qua = [cb for cb in self.danh_sach if ten.lower() in cb.get_ho_ten().lower()]
        if not ket_qua:
            print("Khong tim thay ket qua.")
        return ket_qua

    def hien_thi_ds(self):
        for cb in self.danh_sach:
            print(f"Ten: {cb.get_ho_ten()} | Tuoi: {cb._tuoi} | Dia chi: {cb._dia_chi}")
