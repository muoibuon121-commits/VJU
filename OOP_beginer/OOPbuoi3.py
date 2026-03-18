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

# Định nghĩa điểm -> Sử dụng để định dạng cả Circle và Rect 
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
     def __str__(self):
        return f"({self.x}, {self.y})"
# Viết lớp, Hàm Rect 
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
    # Khoảng cách giữa hai điểm p1, p2  -> căn tổng bình của hiệu 2 thứ -> điểm cần tính khoảng cách
    # và điểm tâm của hình tròn 
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
def point_in_circle(circle, point):
    d = distance(circle.center, point)
    return d <= circle.radius # Hình sẽ đúng nhiều kết quả bé hơn bằng Radius 
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
