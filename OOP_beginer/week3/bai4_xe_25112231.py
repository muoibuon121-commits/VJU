class Car:
    def __init__(self, hang, gia):
        self.hang = hang
        self.gia = gia

    def lai_xe(self):
        print(f"\n🚗 Đang lái chiếc {self.hang}...")
        lua_chon = input("Gặp xe đi láo, đâm không? (có/không): ").lower()
        if lua_chon == "có":
            print("💥 RẦM! Xe có bảo hiểm, lo gì!")
        else:
            print("😇 Nhẫn nhịn là quốc sách, a di đà phật.")

if __name__ == '__main__':
    my_car = Car("VinFast", "1.2 Tỷ")
    my_car.lai_xe()
