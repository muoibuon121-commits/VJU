import math

class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

class Circle:
    def __init__(self, center, radius):
        self.center = center # Center là một object Point
        self.radius = radius

class Rectangle:
    def __init__(self, corner, w, h):
        self.corner = corner # Corner là Point (góc dưới trái)
        self.width, self.height = w, h

def point_in_circle(circle, point):
    d = math.hypot(circle.center.x - point.x, circle.center.y - point.y)
    return d <= circle.radius

def rect_circle_overlap(circle, rect):
    """Kiểm tra xem hình chữ nhật có chạm vào hình tròn không"""
    closest_x = max(rect.corner.x, min(circle.center.x, rect.corner.x + rect.width))
    closest_y = max(rect.corner.y, min(circle.center.y, rect.corner.y + rect.height))
    d = math.hypot(circle.center.x - closest_x, circle.center.y - closest_y)
    return d <= circle.radius

# Test logic
c = Circle(Point(150, 100), 75)
r = Rectangle(Point(100, 50), 200, 200)
print(f"Hình chữ nhật có chạm hình tròn không? -> {rect_circle_overlap(c, r)}")
