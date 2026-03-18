# Bài 1: tính điểm, khoảng cách giữa 2 điểm 
import math 
class point:
    def __init__ (self, x, y):
        self.x = x 
        self.y = y 
        print(f"Đã tạo điểm tại ({self.x}, {self.y})")
    def distance(self, x1, y1):
        return math.hypot(self.x - x1, self.y - y1)
if __name__ == '__main__':
    x = float(input("Nhập tọa độ x của điểm A : "))
    y = float(input("Nhập tọa độ y của điểm A : "))
    Tâm = point (0,0)
    my_circle = point(x, y)
    distance1 = math.hypot(x, y)
    x1 = float(input("Nhập tọa độ x của điểm B: "))
    y1 = float(input("Nhập tọa độ y của điểm B: "))
    distance2 = my_circle.distance(x1, y1)
    print(f"Khoảng cách từ điểm ({x}, {y}) đến gốc toạ độ O là: {distance1:.2f}")
    print(f"Khoảng cách từ điểm B ({x1}, {y1}) đến điểm A ({x}, {y}) là: {distance2:.2f}")
# Bài 2+3: Siêu Nhân Gao 
team = []
class Siêu_Nhân:
    def __init__ (self, ten, vu_khi, mau_sac):
        self.ten = ten 
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
    def __str__(self):
        return f"Gao: {self.ten}, Vũ khí: {self.vu_khi}, Màu sắc: {self.mau_sac}"
if __name__ == '__main__':
    số_siêu_nhân = int(input("Nhập số lượng siêu nhân Gao: "))
    for i in range(số_siêu_nhân):
        print(f"Nhập thông tin siêu nhân Gao {i+1}:")
        siêu_nhân = Siêu_Nhân(input("Nhập tên siêu nhân: "), input("Nhập vũ khí của siêu nhân: "), input("Nhập màu sắc của siêu nhân: "))
        team.append(siêu_nhân)
    print("\n DANH SÁCH SIÊU NHÂN")
    for s in team:
        print(s)
# Bài 4:
# a, bài tập con chó 
chuồng_chó = []
class chó:
    def __init__(self, tên, màu, loài, cảm_xúc):
        self.tên = tên
        self.màu = màu
        self.loài = loài
        self.cảm_xúc = cảm_xúc
    def __str__(self):
        return f"Tên: {self.tên}, Loài: {self.loài}, Màu: {self.màu}, Cảm xúc: {self.cảm_xúc}"
    def chọc_chó(self):
        quyết_định = input(f"Bạn muốn chọc, cho ăn hay vỗ {self.tên}? (chọc/cho ăn/vỗ): ")
        if quyết_định.lower() == "chọc":
            self.cảm_xúc = "tức giận"
            return f"Bạn đã chọc {self.tên}, nó đang {self.cảm_xúc} và sắp cắn bạn, chạy nhanh lên =)) !"
        elif quyết_định.lower() == "cho ăn":
            self.cảm_xúc = "hạnh phúc"
            return f"Bạn đã cho ăn {self.tên}, nó đang {self.cảm_xúc} và vẫy đuôi !"
        elif quyết_định.lower() == "vỗ":
            self.cảm_xúc = "vui vẻ"
            return f"Bạn đã vỗ {self.tên}, nó đang {self.cảm_xúc} và lăn ngửa cho bạn xoa bụng !"
        else:
            return "Quyết định không hợp lệ. Hãy chọn 'chọc', 'cho ăn' hoặc 'vỗ'."
    def sủa(self):
        return f"{self.tên} đang sủa: Gâu gâu!"
    def ăn(self, thức_ăn):
        self.thức_ăn = thức_ăn
        return f"{self.tên} đang ăn {thức_ăn}."
    def chơi(self, đồ_chơi):
        self.đồ_chơi = đồ_chơi
        return f"{self.tên} đang chơi với {đồ_chơi}."
if __name__ == '__main__':
    số_chó = int(input("Nhập số lượng chó: "))
    for i in range(số_chó):
        print(f"\n--- Nhập thông tin bé {i+1} ---")
        cờ_hó = chó(input("Nhập tên chó: "), input("Nhập màu chó: "), input("Nhập loài chó: "), "bình thường")
        chuồng_chó.append(cờ_hó)
    print("\n=== DANH SÁCH CHUỒNG CHÓ ===")
    for c in chuồng_chó:
        print(c)
    if len(chuồng_chó) > 0:
        print("tương tác")
        print(chuồng_chó[0].chọc_chó())
# b, bài tập ô tô 
class car:
    def __init__(self, hãng, kích_thước, màu, giá):
        self.hãng = hãng
        self.kích_thước = kích_thước
        self.màu = màu
        self.giá = giá
    def __str__(self):
        return f"Đã tạo xe {self.hãng} với kích thước {self.kích_thước}, màu {self.màu} và giá {self.giá}"
    def tốc_độ(self):
        điều_chỉnh_tốc_độ = input("Bạn muốn tăng tốc hay giảm tốc ? (tăng/giảm): ")
        if điều_chỉnh_tốc_độ.lower() == "tăng":
            return f"Bạn đã tăng tốc"
        elif điều_chỉnh_tốc_độ.lower() == "giảm":
            return f"Bạn đã giảm tốc"
        else:
            return "Quyết định không hợp lệ. Hãy chọn 'tăng' hoặc 'giảm'."
    def đâm(self):
        print("xe đăng trước chạy hơi láo !")
        suy_nghĩ = input("Bạn có muốn đâm không ? (có/không): ")
        if suy_nghĩ.lower() == "có":
            return f"Bạn đã quyết định đâm, xe đã có bảo hiểm thân vỏ, yên tâm !"
        elif suy_nghĩ.lower() == "không":
            return f"Bạn đã quyết định không đâm, thôi a di đà phật"
        else:
            return "Quyết định không hợp lệ. Hãy chọn 'có' hoặc 'không'."
if __name__ == '__main__':
    số_xe = int(input("Nhập số lượng xe: "))
    for i in range(số_xe):
        print(f"Nhập thông tin xe {i+1}:")
        xe = car(input("Hãng xe: "), input("Kích thước: "), input("Màu: "), input("Giá: "))
        print(xe)
        if i == 0:  # Tương tác với xe đầu tiên
            print(xe.tốc_độ())
            print(xe.đâm())
# c, Tài khoản ngân hàng
class bank_account:
    def __init__(self, tên_tài_khoản, số_tài_khoản, ngân_hàng, số_dư):
        self.tên_tài_khoản = tên_tài_khoản
        self.số_tài_khoản = số_tài_khoản
        self.ngân_hàng = ngân_hàng
        self.số_dư = số_dư
    def __str__(self):
        return f"Tài khoản {self.tên_tài_khoản} tại ngân hàng {self.ngân_hàng} với số tài khoản {self.số_tài_khoản} có số dư {self.số_dư}"
    def thao_tác(self):
        chọn = input("Bạn muốn rút tiền, gửi tiền hay kiểm tra số dư? (rút/gửi/kiểm tra)")
        if chọn.lower() == "rút":
            số_tiền = float(input("Nhập số tiền bạn muốn rút: "))
            if số_tiền > self.số_dư:
                return "Số dư không đủ để rút."
            else:
                self.số_dư -= số_tiền
                return f"Bạn đã rút {số_tiền}. Số dư hiện tại: {self.số_dư}"
        elif chọn.lower() == "gửi":
            số_tiền = float(input("Nhập số tiền bạn muốn gửi: "))
            self.số_dư += số_tiền
            return f"Bạn đã gửi {số_tiền}. Số dư hiện tại: {self.số_dư}"
        elif chọn.lower() == "kiểm tra":
            return f"Số dư hiện tại của bạn là: {self.số_dư}"
        else:
            return "Lựa chọn không hợp lệ. Hãy chọn 'rút', 'gửi' hoặc 'kiểm tra'."
if __name__ == '__main__':
    số_tài_khoản = int(input("Nhập số lượng tài khoản: "))
    for i in range(số_tài_khoản):
        print(f"Nhập thông tin tài khoản {i+1}:")
        tài_khoản = bank_account(input("Tên tài khoản: "), input("Số tài khoản: "), input("Ngân hàng: "), float(input("Số dư: ")))
        print(tài_khoản)
        if i == 0:  
            print(tài_khoản.thao_tác())



# BÀI 5: THINK PYTHON: CHAP 15
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
     def __str__(self):
        return f"({self.x}, {self.y})"
class Rectangle:
    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width # -> Hình chữ nhật {Điểm khởi đầu như 1 đoạ độ, chiều cao y và chiều rộng x dương}
        self.height = height
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
def point_in_circle(circle, point):
    d = distance(circle.center, point)
    return d <= circle.radius 
def rect_in_circle(circle, rect):
    p1 = rect.corner
    p2 = Point(rect.corner.x + rect.width, rect.corner.y)  
    p3 = Point(rect.corner.x, rect.corner.y + rect.height) 
    p4 = Point(rect.corner.x + rect.width, rect.corner.y + rect.height) 
    # 
    return (point_in_circle(circle, p1) and 
            point_in_circle(circle, p2) and 
            point_in_circle(circle, p3) and 
            point_in_circle(circle, p4))
def rect_circle_overlap(circle, rect):
    closest_x = max(rect.corner.x, min(circle.center.x, rect.corner.x + rect.width))
    closest_y = max(rect.corner.y, min(circle.center.y, rect.corner.y + rect.height))
    closest_point = Point(closest_x, closest_y)
    return distance(circle.center, closest_point) <= circle.radius
if __name__ == '__main__':
    center_pt = Point(150, 100)
    my_circle = Circle(center_pt, 75)
    print(f"Đã tạo Circle với tâm {my_circle.center} và bán kính {my_circle.radius}")
    p_inside = Point(150, 150)
    p_outside = Point(300, 300) 
    print(f"\nĐiểm {p_inside} có nằm trong hình tròn? -> {point_in_circle(my_circle, p_inside)}")
    print(f"Điểm {p_outside} có nằm trong hình tròn? -> {point_in_circle(my_circle, p_outside)}")
    rect_inside = Rectangle(Point(130, 80), 30, 30)
    print(f"\nHình chữ nhật nhỏ (130,80) có nằm HOÀN TOÀN trong hình tròn? -> {rect_in_circle(my_circle, rect_inside)}")
    rect_overlap = Rectangle(Point(100, 50), 200, 200) # Hình to hơn hình tròn
    print(f"Hình chữ nhật to có nằm HOÀN TOÀN trong hình tròn? -> {rect_in_circle(my_circle, rect_overlap)}")
    print(f"Hình chữ nhật to có GIAO/CẮT với hình tròn? -> {rect_circle_overlap(my_circle, rect_overlap)}")





# Bài 5
class NhanVien:
    LUONG_MAX = 50000000
    def __init__(self, tenNhanVien, luongCoBan, heSoLuong):
        self.tenNhanVien = tenNhanVien
        self.luongCoBan = luongCoBan
        self.heSoLuong = heSoLuong
    def get_tenNhanVien(self):
        return self.tenNhanVien
    def set_tenNhanVien(self, tenNhanVien):
        self.tenNhanVien = tenNhanVien
    def get_luongCoBan(self):
        return self.luongCoBan
    def set_luongCoBan(self, luongCoBan):
        self.luongCoBan = luongCoBan
    def get_heSoLuong(self):
        return self.heSoLuong   
    def set_heSoLuong(self, heSoLuong):
        self.heSoLuong = heSoLuong
    def tinhLuong(self):
        return self.luongCoBan * self.heSoLuong
    def inTTin(self):
        print("THÔNG TIN NHÂN VIÊN")
        print(f"Tên nhân viên : {self.tenNhanVien}")
        # Dùng :,.0f để định dạng tiền tệ cho dễ nhìn 
        print(f"Lương cơ bản  : {self.luongCoBan:,.0f} VNĐ")
        print(f"Hệ số lương   : {self.heSoLuong}")
        print(f"Tổng lương    : {self.tinhLuong():,.0f} VNĐ")
    def tangLuong(self, delta):
        luong_moi = self.luongCoBan * (self.heSoLuong + delta)
        if luong_moi > NhanVien.LUONG_MAX:
            print(f"Thông báo: Tăng lương thất bại! Mức lương mới ({luong_moi:,.0f}) vượt quá mức tối đa quy định.")
            return False
        else:
            self.heSoLuong += delta
            return True
if __name__ == '__main__':
    nv1 = NhanVien(input("Nhập tên nhân viên: "), float(input("Nhập lương cơ bản (VNĐ): ")), float(input("Nhập hệ số lương: ")))
    nv1.inTTin()
    print("\n=> Đang thử tăng hệ số lương thêm 1.0...")
    ket_qua_1 = nv1.tangLuong(1.0)
    if ket_qua_1:
        print("Tăng lương thành công!")
        nv1.inTTin()
    print("\n=> Đang thử tăng hệ số lương thêm 2.0...")
    ket_qua_2 = nv1.tangLuong(2.0)
    if not ket_qua_2:
        print("Đã bị hệ thống từ chối.")
