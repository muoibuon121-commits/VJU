import math
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
