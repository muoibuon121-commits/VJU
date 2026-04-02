```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'fontSize': '16px'}}}%%
classDiagram
direction TB

class "HangHoa" as HangHoa {
    #ma_hang: String
    #ten_hang: String
    #nha_sx: String
    #gia: float
    +in_ttin()
}

class "HangDienMay" as HangDienMay {
    -tg_baohanh: int
    -dien_ap: int
    -cong_suat: int
    +in_ttin()
}

class "HangSanhSu" as HangSanhSu {
    -loai_nguyenlieu: String
    +in_ttin()
}

class "HangThucPham" as HangThucPham {
    -ngay_sx: String
    -ngay_hethan: String
    +in_ttin()
}

class "QLHangHoa" as QLHangHoa {
    +danh_sach: List
    +them_hang(hang: HangHoa)
    +hien_thi()
    +tim_kiem(ten_tim: String)
}

HangHoa <|-- HangDienMay
HangHoa <|-- HangSanhSu
HangHoa <|-- HangThucPham
QLHangHoa "1" o-- "0..*" HangHoa : quan_ly


class "CanBo" as CanBo {
    -hoten: String
    -tuoi: int
    -gioitinh: String
    -diachi: String
    +get_hoten(): String
    +inTTin()
}

class "CongNhan" as CongNhan {
    -bac: int
    +inTTin()
}

class "KySu" as KySu {
    -nganhdaotao: String
    +inTTin()
}

class "NhanVienCB" as NhanVienCB {
    -congviec: String
    +inTTin()
}

class "QLCB" as QLCB {
    +danhsach: List
    +addCB(canbo: CanBo)
    +timKiem(ten: String)
    +hienthids()
}

CanBo <|-- CongNhan
CanBo <|-- KySu
CanBo <|-- NhanVienCB
QLCB "1" o-- "0..*" CanBo : quan_ly
