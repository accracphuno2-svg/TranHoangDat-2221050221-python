import vidu2
x = int(input("Nhap so thu nhat: "))
y = int(input("Nhap so thu hai: "))
print("Tong hai so la: ", vidu2.cong(x,y))
print("Hieu hai so la: ", vidu2.tru(x,y))
print("Tich hai so la: ", vidu2.nhan(x,y))

#lenh from..import
from vidu2 import cong, tru
x = int(input("Nhap so thu nhat: "))
y = int(input("Nhap so thu hai: "))
print("Tong hai so la: ", cong(x,y))
print("Hieu hai so la: ", tru(x,y))

#lenh from...import*
from vidu2 import*
x = int(input("Nhap so thu nhat: "))
y = int(input("Nhap so thu hai: "))
print("Tong hai so la: ", cong(x,y))
print("Hieu hai so la: ", tru(x,y))
print("Tich hai so la: ", nhan(x,y))
print("Thuong hai so la: ", chia(x,y))