
import math
import time 
# CHAPTER 1: 
print("1.1.Có bao nhiêu giây trong 42 phút 42 giây -> có bao nhiêu giây trong m phút n giây")
m = float(input("Nhập số phút: "))
n = int(input("Nhập số giây: "))
print(f"Số giây trong {m} phút và {n} giây là: {m*60+n}")
print("1.2.Chuyển đổi 10 KM sang miles, biết 1 mile bằng 1.61 km -> nhập số x km sau đó chuyển sang mile/miles")
x = float(input("nhập số kilometers:"))
y = x/1.61
if y ==1:
    print(f"{x} km bằng {y} mile")
else:
    print(f"{x} km bằng {y} miles") # khi bằng 1 sẽ là mile, trên và dưới 1 đều là miles
print(" 1.3. Nếu bạn chạy 10 cây trong 42 phút và 42 giây thì trung bình tốc độ là bao nhiêu ? -> nhập khoảng cách chạy Q và thời gian chạy m.n ")
Q = float(input("Nhập số KM đã chạy:"))/1.61
m = float(input("Nhập số phút đã chạy:"))
n = float(input("NHập số giây đã chạy:"))
print(f"PACE là {(m+n/60)/Q} mile/minutes ") # Tính PACE 
print(f"Tốc độ trung bình là {(m*60+n)/Q} mile/seconds ") # Tính PACE 
print(f"Tốc độ trung bình là {Q/((m*60+n)/3600):.2f} mile/hours ") # Tính SPEED / :.2f làm tròn cho đẹp :> 
# END CHAP 1 
# CHAPTER 2
print("2.1 Thể tích của hình có bán kính r là bao nhiêu ?")
P = (float(input("nhập bán kính:"))**3)*(4/3)*math.pi
print(f"thể tích của hình cầu là: {P:.2f}")
print("2.1 Giá 1 cuốn sách là 24.95$, nhưng được giảm giá 40%, phí vận chuyển là 3$ cho 1 cuốn đầu và các cuốn sau là 75 cents -> nhập số sách cần mua")
sach = (input("Nhập số sách cần mua:"))
if sach.isdigit():
    S = int(sach)
    if S >= 1:
        print(f"Tổng số tiền là: {(S*24.95*0.6)+ 3 + ((S-1)*0.75):.2f} Đô")
    else: 
        print("Em không bán sách nửa cuốn sách anh ạ!")
else:
    print("Em không bán nửa cuốn đâu !")
print("2.3 Nếu rời khỏi nhà lúc 6h52 và chạy 1 dặm dễ với PACE là 8p15s và 3 dặm sau đó với PACE 7p12s và thêm 1 dặm dễ nữa thì mấy giờ về đến nhà ? -> chuyển về nhập biến") 
TIME1 = float(input("Nhập giờ xuất phát: "))
TIME2 = float(input("Nhập phút xuất phát: ")) 
EASYRUN1 = float(input("Nhập số dặm chạy dễ ban đầu: "))
MIDRUN = float (input("Nhập số dặm chạy bình thường: "))
EASYRUN2 = float(input("Nhập số dặm chạy dễ lúc sau: "))
TIMEEND = TIME1*60*60+TIME2*60 + EASYRUN1*((8*60)+15) + MIDRUN*(7*60+12) + EASYRUN2*(8*60+15)
if TIME1 >= 0 and TIME2 >= 0 and EASYRUN1 >0 and MIDRUN >= 0 and EASYRUN2 >= 0:
    HOUR = int(TIMEEND // 3600 % 24 )
    MINUTE = int(TIMEEND % 3600 // 60)
    SECOND = int(TIMEEND % 60 )
    print(f"Bạn về ăn sáng lúc: {HOUR:02d}:{MINUTE:02d}:{SECOND:02d}")
else: 
    print("Nhập sai rồi bố ơi !")
#END CHAP 2
print ("3.1")
# CHAPTTER 3: 
# 3.1 
# + - - - - + - - - - + -> 2 hàng 2 cột -> gồm 1 dấu cộng + 4 dấu trừ + 4 dấu cộng .....
# |         |         |
# |         |         | -> 4 hàng có gạch + 4 ký tự trống + gạch .....
# |         |         |
# |         |         |
# + - - - - + - - - - + -> tương tự 
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - + -> dùng code để in cái này ra 
Dong = '+' + '-'*4 + '+' + '-'*4 + '+'
XuongDong = '|' + ' '*4 + '|' + ' '*4 + '|'
def ve1():
    print(Dong)
    for i in range(4):
        print(XuongDong)
    print(Dong)
    for i in range(4):
        print(XuongDong)
    print(Dong)
ve1()
print(" 3.2 Viết 1 hàm vẽ lưới tương tự với 4 hàng và 4 cột -> chuyển sang dạng n cột, n hàng ")
S_LINE = '+' + '-'*4 
E_LINE = '+'
S_BLOCK = '|' + ' '*4 
E_BLOCK = '|'
Hang = int(input("Nhập số hàng: "))
Cot = int(input("Nhập số cột: "))
def ve2():
    for _ in range (Cot):
        for _ in range (Hang):
            print(S_LINE, end='') # thay '\n' sang ''
        print(E_LINE)
        for _ in range (4):
            for _ in range (Hang):
                print(S_BLOCK, end='')
            print(E_BLOCK)
    for _ in range (Hang):
        print(S_LINE, end='') # thay '\n' sang ''
    print(E_LINE)
ve2()
# END CHAP 3
# CHAPPTER 5:
print("5.1")
sumtime = time.time()
giây = 60
phút = 60*giây
giờ = 60*phút
ngày = 24*giờ
số_ngày = int(sumtime // ngày)
giây_còn_lại = sumtime % ngày
số_giờ = int(giây_còn_lại // giờ)
giây_còn_lại = giây_còn_lại % giờ
số_phút = int(giây_còn_lại // phút)
giây_còn_lại = giây_còn_lại % phút
số_giây = int(giây_còn_lại)
print(f"Số ngày đã trôi qua kể từ Epoch: {số_ngày} ngày")
print(f"Thời gian hiện tại (GMT): {số_giờ:02d}:{số_phút:02d}:{số_giây:02d}") 
print(f"Thời gian hiện tại (Việt Nam): {(số_giờ + 7) % 24:02d}:{số_phút:02d}:{số_giây:02d}")
# END CHAP 5 
