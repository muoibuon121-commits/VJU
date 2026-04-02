# OOP HOMEWORK - CSE 3011 - DR. Bùi Huy Kiên  
![VJU](https://img.shields.io/badge/University-VJU-red?style=flat&logo=bookstack&logoColor=white) ![Homework](https://img.shields.io/badge/Task-Homework-orange?style=flat&logo=googlesheets&logoColor=white) ![Python](https://img.shields.io/badge/Language-Python-3776AB?style=flat&logo=python&logoColor=white)
# Tech Stack
> - ***IDE*** ` ANTIGRAVITY `
> - ***Lang*** ` Python: 3.x `
> - ***Interpreter*** ` Standard Python Environment `
> - ***Modlues/Libraries*** ` time, math,.. `
# Structure
# OOP_Beginner
``` 
|- Week1/
|  |- OOPbuoi1.py - Print Hello World
`- Week2
|   |- OOPbuoi2.py - Time conversion, distance conversion, pace, speed
|                  - Sphere volume, wholesale cost, breakfast time
|                  - Draw 2x2 and 4x4 text grids
|                  - Epoch time, days since 01/01/1970
`- Week3/
    |- OOPbuoi3.py        - Create Point class, calculate distance between
                          2 points and to the origin (0,0)
                          - Gao Ranger class, manage team list, attributes (weapons, colors)
                          and display
                          - Dog kennel simulation: interact (poke, feed, pet)
                          and update emotional states
                          - Car driving simulation: adjust speed, handle crash decisions
                          - Bank account management: deposit, withdraw, and check balance
                          - 2D Geometry (Think Python Chap 15): Point, Circle,
                          Rectangle classes
                          - Check if a point or rectangle is completely inside a circle
                          - Check intersection/overlap between a circle and a rectangle
                          - Employee class with private attributes (Encapsulation)
                          and static constants
                          - Calculate total salary based on base salary and multiplier
                          - Conditional salary raise: validate against maximum salary limit
```
# How to run ? - Run the ur own way :> !
# Author 
- Name: Trần Ngô Tiến Đạt
- VJU's ID: 25112231
- DM: None
```mermaid
classDiagram
    %% Khối Quản lý Hàng hóa
    class HangHoa {
        #String _ma_hang
        #String _ten_hang
        #String _nha_sx
        #float _gia
        +in_ttin()
    }

    class HangDienMay {
        -int __tg_baohanh
        -int __dien_ap
        -int __cong_suat
        +in_ttin()
    }

    class HangSanhSu {
        -String __loai_nguyenlieu
        +in_ttin()
    }

    class HangThucPham {
        -String __ngay_sx
        -String __ngay_hethan
        +in_ttin()
    }

    class QLHangHoa {
        +List danh_sach
        +them_hang(HangHoa hang)
        +hien_thi()
        +tim_kiem(String ten_tim)
    }

    HangHoa <|-- HangDienMay
    HangHoa <|-- HangSanhSu
    HangHoa <|-- HangThucPham
    QLHangHoa "1" o-- "0..*" HangHoa : quản lý

    %% Khối Quản lý Cán bộ
    class CanBo {
        -String __hoten
        -int __tuoi
        -String __gioitinh
        -String __diachi
        +get_hoten() String
        +inTTin()
    }

    class CongNhan {
        -int __bac
        +inTTin()
    }

    class KySu {
        -String __nganhdaotao
        +inTTin()
    }

    class NhanVienCB {
        -String __congviec
        +inTTin()
    }

    class QLCB {
        +List danhsach
        +addCB(CanBo canbo)
        +timKiem(String ten)
        +hienthids()
    }

    CanBo <|-- CongNhan
    CanBo <|-- KySu
    CanBo <|-- NhanVienCB
    QLCB "1" o-- "0..*" CanBo : quản lý
