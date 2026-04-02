```mermaid
classDiagram
    class Point {
        +float x
        +float y
        +__init__(x, y)
        +__str__() String
    }

    class LineSegment {
        -Point __d1
        -Point __d2
        +__init__(*args)
        +getD1() Point
        +getD2() Point
        +__str__() String
    }

    class NhanVien {
        +int LUONG_MAX$
        -String __ten_nv
        -int __luong_cb
        -float __he_so
        +__init__(ten_nv, luong_cb, he_so)
        +set_he_so(he_so)
        +get_ten_nv() String
        +get_luong_cb() int
        +get_he_so() float
        +tinh_luong() float
        +in_ttin()
        +tang_luong() bool
    }

    LineSegment "1" *-- "2" Point : chứa (Composition)
```
