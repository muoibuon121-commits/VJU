import math 

class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        print(f" Đã tạo điểm tại ({self.x}, {self.y})")

    def distance(self, other_point):
        """Tính khoảng cách đến một object Point khác"""
        return math.hypot(self.x - other_point.x, self.y - other_point.y)

if __name__ == '__main__':
    # Nhập điểm A
    xa = float(input("Nhập x của A: "))
    ya = float(input("Nhập y của A: "))
    pt_a = Point(xa, ya)
    
    # Tính khoảng cách tới gốc tọa độ O(0,0)
    origin = Point(0, 0)
    print(f"Khoảng cách A -> O: {pt_a.distance(origin):.2f}")
    
    # Nhập điểm B và tính A -> B
    xb = float(input("Nhập x của B: "))
    yb = float(input("Nhập y của B: "))
    pt_b = Point(xb, yb)
    print(f"Khoảng cách A -> B: {pt_a.distance(pt_b):.2f}")
