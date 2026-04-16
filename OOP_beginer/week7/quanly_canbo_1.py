import csv
import json
import os


class CanBo:


    def __init__(self, ho_ten="", tuoi=0, gioi_tinh="", dia_chi=""):
        self.ho_ten = ho_ten.strip()
        try:
            self.tuoi = int(tuoi)
        except (ValueError, TypeError):
            self.tuoi = 0
        self.gioi_tinh = gioi_tinh.strip()
        self.dia_chi = dia_chi.strip()

    def get_ho_ten(self):
        return self.ho_ten

    def get_loai(self):
        return "CanBo"

    def get_luong(self):
        """Luong de so sanh - lop con override"""
        return 0

    # ---- Yeu cau 3: to_dict / from_dict ----
    def to_dict(self):
        return {
            "loai": self.get_loai(),
            "ho_ten": self.ho_ten,
            "tuoi": self.tuoi,
            "gioi_tinh": self.gioi_tinh,
            "dia_chi": self.dia_chi,
        }

    @staticmethod
    def from_dict(d):
        """Factory: khoi phuc dung lop con dua vao truong 'loai'."""
        loai = d.get("loai", "CanBo")
        ho_ten = d.get("ho_ten", "")
        tuoi = d.get("tuoi", 0)
        gt = d.get("gioi_tinh", "")
        dc = d.get("dia_chi", "")

        if loai == "CongNhan":
            return CongNhan(ho_ten, tuoi, gt, dc, d.get("bac", 1))
        if loai == "KySu":
            return KySu(ho_ten, tuoi, gt, dc, d.get("nganh", ""))
        if loai == "NhanVien":
            return NhanVien(ho_ten, tuoi, gt, dc, d.get("cong_viec", ""))
        return CanBo(ho_ten, tuoi, gt, dc)

    def __str__(self):
        return (f"{self.ho_ten:22s} | Tuoi:{self.tuoi:3d} | "
                f"GT:{self.gioi_tinh:4s} | DC:{self.dia_chi:14s}")


class CongNhan(CanBo):
    # Cong nhan - phan biet theo bac (1..10).
    LUONG_CO_BAN = 2_340_000  # VND/bac

    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        try:
            bac = int(bac)
        except (ValueError, TypeError):
            bac = 1
        self.bac = bac if 1 <= bac <= 10 else 1

    def get_loai(self):
        return "CongNhan"

    def get_luong(self):
        return self.bac * self.LUONG_CO_BAN

    def to_dict(self):
        d = super().to_dict()
        d["bac"] = self.bac
        return d

    def __str__(self):
        return (super().__str__() +
                f" | CongNhan | Bac:{self.bac:2d} | Luong:{self.get_luong():>12,.0f}")


class KySu(CanBo):
    # Ky su - phan biet theo nganh.
    LUONG_CO_BAN = 15_000_000

    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh = nganh.strip()

    def get_loai(self):
        return "KySu"

    def get_luong(self):
        return self.LUONG_CO_BAN

    def to_dict(self):
        d = super().to_dict()
        d["nganh"] = self.nganh
        return d

    def __str__(self):
        return (super().__str__() +
                f" | KySu     | Nganh:{self.nganh:18s} | Luong:{self.get_luong():>12,.0f}")


class NhanVien(CanBo):
    # Nhan vien - phan biet theo cong viec.
    LUONG_CO_BAN = 10_000_000

    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec.strip()

    def get_loai(self):
        return "NhanVien"

    def get_luong(self):
        return self.LUONG_CO_BAN

    def to_dict(self):
        d = super().to_dict()
        d["cong_viec"] = self.cong_viec
        return d

    def __str__(self):
        return (super().__str__() +
                f" | NhanVien | CV:{self.cong_viec:18s}    | Luong:{self.get_luong():>12,.0f}")


class QuanLyCanBo:


    def __init__(self, csv_file="canbo.csv", json_file="canbo.json"):
        self.csv_file = csv_file
        self.json_file = json_file
        # Yeu cau 2: luu vao dict, key = ho_ten
        self.ds_dict = {}

        # Uu tien JSON neu co, ngu quoc lui ve CSV
        if os.path.exists(self.json_file):
            self.load_json()
        elif os.path.exists(self.csv_file):
            self.load_csv()
            self.save_json()  # lan dau chuyen CSV -> JSON

    def load_csv(self):
        """Doc CSV, xu ly FileNotFoundError va ValueError cho tung dong."""
        loaded, skipped = 0, 0
        try:
            with open(self.csv_file, "r", encoding="utf-8", newline="") as f:
                reader = csv.reader(f)
                next(reader, None)  # bo qua header
                for idx, row in enumerate(reader, start=2):
                    if not row or len(row) < 6:
                        print(f"  [!] Dong {idx} thieu cot, bo qua: {row}")
                        skipped += 1
                        continue
                    try:
                        ho_ten = row[0].strip()
                        tuoi = int(row[1].strip())        # co the gay ValueError
                        gt = row[2].strip()
                        dc = row[3].strip()
                        loai = row[4].strip()
                        extra = row[5].strip()

                        if loai == "CongNhan":
                            cb = CongNhan(ho_ten, tuoi, gt, dc, int(extra))
                        elif loai == "KySu":
                            cb = KySu(ho_ten, tuoi, gt, dc, extra)
                        elif loai == "NhanVien":
                            cb = NhanVien(ho_ten, tuoi, gt, dc, extra)
                        else:
                            print(f"  [!] Dong {idx} loai khong ro '{loai}', bo qua.")
                            skipped += 1
                            continue

                        self.ds_dict[ho_ten] = cb
                        loaded += 1
                    except ValueError as e:
                        print(f"  [!] Dong {idx} loi ValueError ({e}), bo qua: {row}")
                        skipped += 1
                    except Exception as e:
                        print(f"  [!] Dong {idx} loi {type(e).__name__}: {e}, bo qua.")
                        skipped += 1
            print(f"[OK] Doc CSV: nap {loaded} ban ghi, bo qua {skipped}.")
        except FileNotFoundError:
            print(f"[!] Khong tim thay file CSV: {self.csv_file}")
        except Exception as e:
            print(f"[!] Loi khi doc CSV ({type(e).__name__}): {e}")

    def them(self, cb):
        if not isinstance(cb, CanBo):
            print("[!] Doi tuong khong hop le.")
            return False
        if not cb.ho_ten:
            print("[!] Ho ten trong.")
            return False
        if cb.ho_ten in self.ds_dict:
            print(f"[!] '{cb.ho_ten}' da ton tai.")
            return False
        self.ds_dict[cb.ho_ten] = cb
        self.save_json()
        print(f"[OK] Da them: {cb.ho_ten}")
        return True

    def xoa(self, ho_ten):
        if ho_ten in self.ds_dict:
            del self.ds_dict[ho_ten]
            self.save_json()
            print(f"[OK] Da xoa: {ho_ten}")
            return True
        print(f"[!] Khong tim thay: {ho_ten}")
        return False

    def tim_theo_ten(self, ten):
        t = ten.lower().strip()
        return [cb for cb in self.ds_dict.values() if t in cb.ho_ten.lower()]

    def tim_theo_loai(self, loai):
        return [cb for cb in self.ds_dict.values() if cb.get_loai() == loai]

    def top3_luong_cao_nhat(self):
        return sorted(self.ds_dict.values(),
                      key=lambda x: x.get_luong(),
                      reverse=True)[:3]

    def hien_thi_tat_ca(self):
        if not self.ds_dict:
            print("  (Danh sach rong)")
            return
        for i, cb in enumerate(self.ds_dict.values(), 1):
            print(f"  {i:2d}. {cb}")

    def save_json(self):
        try:
            data = [cb.to_dict() for cb in self.ds_dict.values()]
            with open(self.json_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"[!] Loi luu JSON ({type(e).__name__}): {e}")

    def load_json(self):
        try:
            with open(self.json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.ds_dict.clear()
            for d in data:
                cb = CanBo.from_dict(d)
                self.ds_dict[cb.ho_ten] = cb
            print(f"[OK] Da tai {len(self.ds_dict)} can bo tu {self.json_file}")
        except FileNotFoundError:
            print(f"[!] Khong tim thay: {self.json_file}")
        except (json.JSONDecodeError, ValueError) as e:
            print(f"[!] JSON khong hop le: {e}")
        except Exception as e:
            print(f"[!] Loi tai JSON ({type(e).__name__}): {e}")

    def menu(self):
        actions = {
            "1": ("Hien thi tat ca",                 self._act_hien_thi),
            "2": ("Them can bo",                     self._act_them),
            "3": ("Xoa theo ho ten",                 self._act_xoa),
            "4": ("Tim theo ho ten",                 self._act_tim_ten),
            "5": ("Tim theo loai (CongNhan/KySu/NV)", self._act_tim_loai),
            "6": ("Top 3 bac/luong cao nhat",        self._act_top3),
            "7": ("Nap lai tu CSV",                  self._act_reload_csv),
            "8": ("Luu ngay ra JSON",                self._act_save_now),
            "0": ("Thoat",                           None),
        }
        while True:
            print("\n" + "=" * 52)
            print("  CHUONG TRINH QUAN LY CAN BO")
            print("=" * 52)
            for k, (label, _) in actions.items():
                print(f"   {k}. {label}")
            try:
                ch = input(" Chon: ").strip()
                if ch == "0":
                    print("Tam biet!")
                    break
                if ch in actions and actions[ch][1]:
                    actions[ch][1]()
                else:
                    print("[!] Lua chon khong hop le.")
            except (KeyboardInterrupt, EOFError):
                print("\nTam biet!")
                break
            except Exception as e:
                # Chuong trinh KHONG crash du co bat ky loi nao
                print(f"[!] Loi khong xac dinh ({type(e).__name__}): {e}")

    @staticmethod
    def _nhap_int(prompt):
        while True:
            s = input(prompt).strip()
            try:
                return int(s)
            except ValueError:
                print("   Vui long nhap so nguyen.")

    def _act_hien_thi(self):
        print(f"\n>>> Danh sach ({len(self.ds_dict)} can bo):")
        self.hien_thi_tat_ca()

    def _act_them(self):
        try:
            ho_ten = input(" Ho ten: ").strip()
            if not ho_ten:
                print("[!] Ho ten khong duoc trong.")
                return
            tuoi = self._nhap_int(" Tuoi: ")
            gt = input(" Gioi tinh (Nam/Nu): ").strip()
            dc = input(" Dia chi: ").strip()
            print(" Loai: 1.CongNhan  2.KySu  3.NhanVien")
            c = input(" Chon (1/2/3): ").strip()
            if c == "1":
                cb = CongNhan(ho_ten, tuoi, gt, dc, self._nhap_int(" Bac (1-10): "))
            elif c == "2":
                cb = KySu(ho_ten, tuoi, gt, dc, input(" Nganh: ").strip())
            elif c == "3":
                cb = NhanVien(ho_ten, tuoi, gt, dc, input(" Cong viec: ").strip())
            else:
                print("[!] Loai khong hop le.")
                return
            self.them(cb)
        except Exception as e:
            print(f"[!] Khong the them ({type(e).__name__}): {e}")

    def _act_xoa(self):
        self.xoa(input(" Ho ten can xoa: ").strip())

    def _act_tim_ten(self):
        kq = self.tim_theo_ten(input(" Ten can tim: ").strip())
        print(f"\n>>> {len(kq)} ket qua:")
        for cb in kq:
            print(f"   - {cb}")

    def _act_tim_loai(self):
        loai = input(" Loai (CongNhan/KySu/NhanVien): ").strip()
        kq = self.tim_theo_loai(loai)
        print(f"\n>>> {len(kq)} {loai}:")
        for cb in kq:
            print(f"   - {cb}")

    def _act_top3(self):
        kq = self.top3_luong_cao_nhat()
        print("\n>>> Top 3 bac/luong cao nhat:")
        for i, cb in enumerate(kq, 1):
            print(f"   #{i}: {cb}")

    def _act_reload_csv(self):
        self.ds_dict.clear()
        self.load_csv()
        self.save_json()

    def _act_save_now(self):
        self.save_json()
        print(f"[OK] Da luu {len(self.ds_dict)} ban ghi vao {self.json_file}")


if __name__ == "__main__":
    app = QuanLyCanBo("canbo.csv", "canbo.json")
    app.menu()
