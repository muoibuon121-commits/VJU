``` mermaid
graph TD
    %% Định nghĩa các lớp
    HH[<b>HangHoa</b><br/>#ma_hang, #ten_hang, #gia<br/>+in_ttin]
    DM[<b>HangDienMay</b><br/>-tg_baohanh, -dien_ap<br/>+in_ttin]
    SS[<b>HangSanhSu</b><br/>-loai_nguyenlieu<br/>+in_ttin]
    TP[<b>HangThucPham</b><br/>-ngay_sx, -ngay_hethan<br/>+in_ttin]
    QL[<b>QLHangHoa</b><br/>+List danh_sach<br/>+them_hang, +tim_kiem]

    %% Quan hệ
    HH <|-- DM
    HH <|-- SS
    HH <|-- TP
    QL o-- HH
    
    %% Định dạng màu sắc cho dễ nhìn
    style HH fill:#f9f,stroke:#333,stroke-width:2px
    style QL fill:#bbf,stroke:#333,stroke-width:2px
graph TD
    %% Định nghĩa các lớp
    CB[<b>CanBo</b><br/>-hoten, -tuoi, -diachi<br/>+get_hoten, +inTTin]
    CN[<b>CongNhan</b><br/>-bac<br/>+inTTin]
    KS[<b>KySu</b><br/>-nganhdaotao<br/>+inTTin]
    NV[<b>NhanVienCB</b><br/>-congviec<br/>+inTTin]
    QL[<b>QLCB</b><br/>+List danhsach<br/>+addCB, +timKiem]

    %% Quan hệ
    CB <|-- CN
    CB <|-- KS
    CB <|-- NV
    QL o-- CB

    %% Định dạng màu sắc
    style CB fill:#f96,stroke:#333,stroke-width:2px
    style QL fill:#9f9,stroke:#333,stroke-width:2px
