from ChuyenNganh import *

class Khoa:
    __tenKhoa= None
    __CacChuyenNganh = []

    def __init__(self,a ,*b):
        self.__tenKhoa =a
        for i in b:
            self.__CacChuyenNganh.append(i)

    def __str__(self):
        print ("Ten khoa: %s\nDanh sach cac chuyen nganh:" %(self.__tenKhoa))      
        for i in self.__CacChuyenNganh:
            print(i)
        return ""  

    def __del__(self):
        del self.__tenKhoa
        for i in self.getCacKhoa():
            del i

    # setters
    def setTenKhoa(self, tenKhoa):
        self.__tenKhoa = tenKhoa

    def setCacChuyenNganh(self, *cacChuyenNganh):
        self.__CacChuyenNganh = cacChuyenNganh

    # getters
    def getTenKhoa(self):
        return self.__tenKhoa

    def getCacKhoa(self):
        return self.__CacChuyenNganh

    def ThemKhoa():
        return Khoa(input("Nhập tên khoa: "), *input("Nhập cac chuyên ngành: "))
    def SuaTT(self):
        print("Sua thong tin khoa: % s" % self.getTenKhoa())
        print("1.Sua ten khoa\n2.Sua chuyen nghanh\n3.Done")
        choose = input("Chon thao tac(1, 2): ")
        while True:
            if choose == "1":
                self.__tenKhoa = input("Nhap ten khoa moi: ")
                break
            elif choose == "2":
                self.__CacChuyenNganh.suaTT()
                break
            else:
                break;
        print("Thong tin sau khi sua\n% s:" % self)

a =ChuyenNganh("KHoa hoc may tinh", "TI")
b= ChuyenNganh("he thong thong tin", "TE")
c= ChuyenNganh("toan ung dung", "TM")


x= Khoa("toán tin", a,b,c)
print(x)
x.SuaTT()
print(x)
