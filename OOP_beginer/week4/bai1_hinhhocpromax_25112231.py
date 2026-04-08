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
        1. Không tham số: Tạo đoạn thẳng mặc định từ (8,5) đến (1,0)
        2. 1 tham số (LineSegment): Sao chép từ một đoạn thẳng khác
        3. 2 tham số (Point, Point): Tạo từ hai đối tượng điểm
        4. 4 tham số (x1, y1, x2, y2): Tạo từ tọa độ số thực
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
        return f'Đoạn thẳng từ {self.__d1} đến {self.__d2}'

if __name__ == "__main__":
    print("--- KIỂM TRA LỚP ĐOẠN THẲNG ---")
    l1 = LineSegment()
    print(f"Mặc định: {l1}")

    l2 = LineSegment(Point(3, 4), Point(5, 6))
    print(f"Từ 2 Point: {l2}")

    l3 = LineSegment(7, 8, 9, 10)
    print(f"Từ 4 tọa độ: {l3}")

    l4 = LineSegment(l2)
    print(f"Sao chép từ l2: {l4}")
