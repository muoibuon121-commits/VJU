![Sơ đồ Hàng hóa](https://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/plantuml/plantuml/master/src/docs/classes.puml&fmt=svg&inline=true&uml=
@startuml
skinparam classAttributeIconSize 0
class HangHoa {
  #ma_hang: String
  #ten_hang: String
  #nha_sx: String
  #gia: float
  +in_ttin()
}
class HangDienMay {
  -tg_baohanh: int
  -dien_ap: int
  -cong_suat: int
}
class HangSanhSu {
  -loai_nguyenlieu: String
}
class HangThucPham {
  -ngay_sx: String
  -ngay_hethan: String
}
class QLHangHoa {
  +danh_sach: List
  +them_hang()
  +tim_kiem()
}
HangHoa <|-- HangDienMay
HangHoa <|-- HangSanhSu
HangHoa <|-- HangThucPham
QLHangHoa o-- HangHoa
@enduml
)
