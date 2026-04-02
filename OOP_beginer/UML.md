``` mermaid
classDiagram
    direction TB
    class HangHoa {
        #String _ma_hang
        #String _ten_hang
        #float _gia
        +in_ttin()
    }
    class HangDienMay {
        -int __tg_baohanh
        +in_ttin()
    }
    class HangSanhSu {
        -String __loai_nguyenlieu
        +in_ttin()
    }
    class HangThucPham {
        -String __ngay_hethan
        +in_ttin()
    }
    class QLHangHoa {
        +List danh_sach
        +them_hang()
    }

    HangHoa <|-- HangDienMay
    HangHoa <|-- HangSanhSu
    HangHoa <|-- HangThucPham
    QLHangHoa o-- HangHoa
