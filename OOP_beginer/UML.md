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
        -int __dien_ap
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
        +them_hang(HangHoa)
    }

    HangHoa <|-- HangDienMay : Thừa kế
    HangHoa <|-- HangSanhSu : Thừa kế
    HangHoa <|-- HangThucPham : Thừa kế
    QLHangHoa o-- HangHoa : Quản lý
