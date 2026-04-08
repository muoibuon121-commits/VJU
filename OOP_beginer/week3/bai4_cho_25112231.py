class Cho:
    def __init__(self, ten, mau, loai):
        self.ten = ten
        self.mau = mau
        self.loai = loai
        self.cam_xuc = "bình thường"

    def tuong_tac(self):
        cmd = input(f"Làm gì với {self.ten}? (chọc/ăn/vỗ): ").lower()
        if cmd == "chọc":
            self.cam_xuc = "tức giận"
            print(f"💢 {self.ten} đang {self.cam_xuc}, CHẠY MAU!")
        elif cmd == "ăn":
            self.cam_xuc = "hạnh phúc"
            print(f"🦴 {self.ten} đang {self.cam_xuc}, vẫy đuôi tít mù!")
        elif cmd == "vỗ":
            self.cam_xuc = "vui vẻ"
            print(f"🐶 {self.ten} đang {self.cam_xuc}, nằm ngửa chờ xoa bụng.")

if __name__ == '__main__':
    my_dog = Cho("Lu", "Vàng", "Cỏ")
    my_dog.tuong_tac()
