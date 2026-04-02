import copy
class Point: 
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'
class LineSegment:
    def __init__(self, *args):
        """
        Khởi tạo đa năng:
        - Không tham số: (8,5) -> (1,0)
        - 1 tham số: Sao chép từ LineSegment khác
        - 2 tham số: Hai đối tượng Point
        - 4 tham số: x1, y1, x2, y2
        """
        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)
        elif len(args) == 1 and isinstance(args[0], LineSegment):
            self.__d1 = copy.deepcopy(args[0].getD1())
            self.__d2 = copy.deepcopy(args[0].getD2())
        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
            self.__d1 = args[0]
            self.__d2 = args[1]
        elif len(args) == 4:
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])
        else:
            self.__d1 = Point(0, 0)
            self.__d2 = Point(0, 0)

    def getD1(self): return self.__d1
    def getD2(self): return self.__d2

    def __str__(self):
        return f'{self.__d1} và {self.__d2}'

class NhanVien:
    LUONG_MAX = 360000000
    
    def __init__(self, ten_nv="", luong_cb=0, he_so=0.0):
        self.__ten_nv = ten_nv
        self.__luong_cb = luong_cb
        self.__he_so = he_so

    def set_he_so(self, he_so):
        self.__he_so = he_so

    def get_ten_nv(self): return self.__ten_nv
    def get_luong_cb(self): return self.__luong_cb
    def get_he_so(self): return self.__he_so

    def tinh_luong(self):
        return self.__luong_cb * self.__he_so

    def in_ttin(self):
        print(f"--- Thông tin nhân viên ---")
        print(f"Tên: {self.get_ten_nv()}")
        print(f"Lương thực nhận: {self.__luong_cb} x {self.__he_so} = {self.tinh_luong():,.0f} VNĐ")

    def tang_luong(self):
        try:
            he_so_tang = float(input(f"Nhập hệ số tăng thêm cho {self.__ten_nv}: "))
            luong_moi = self.__luong_cb * (self.__he_so + he_so_tang)
            
            if luong_moi > self.LUONG_MAX:
                print("Lỗi: Lương sau khi tăng vượt mức cho phép!")
                return False
            else:
                self.__he_so += he_so_tang
                print(f" Tăng lương thành công. Hệ số mới: {self.__he_so}")
                return True
        except ValueError:
            print(" Lỗi: Vui lòng nhập số hợp lệ.")
            return False
if __name__ == "__main__":
    print("--- KIỂM TRA LỚP NHÂN VIÊN ---")
    nv1 = NhanVien("Muối", 8100000, 5.5)
    nv1.in_ttin()
    nv1.tang_luong()
    nv1.in_ttin()
    print("\n")
    print("KIỂM TRA LỚP ĐOẠN THẲNG")
    l1 = LineSegment()
    print(f"l1 (Mặc định): {l1}")

    l2 = LineSegment(Point(3, 4), Point(5, 6))
    print(f"l2 (Từ 2 Point): {l2}")

    l3 = LineSegment(7, 8, 9, 10)
    print(f"l3 (Từ 4 tọa độ): {l3}")

    l4 = LineSegment(l2)
    print(f"l4 (Sao chép từ l2): {l4}")
