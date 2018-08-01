from ChuyenNganh import *

class Khoa:
    __tenKhoa= None
    __CacChuyenNganh = []
    __soLuongCacChuyenNganh =0

    def __init__(self,a ,*b):
        self.__tenKhoa =a
        for i in b:
            self.__CacChuyenNganh.append(i)
            self.__soLuongCacChuyenNganh+=1
        #self.__CacChuyenNganh =b;
    def __str__(self):
        print ("Ten khoa: %s\nDanh sach cac chuyen nganh:" %(self.__tenKhoa))      
        for i in self.__CacChuyenNganh:
            print(i)
        return ""    

a =ChuyenNganh("KHoa hoc may tinh", "TI")
b= ChuyenNganh("he thong thong tin", "TE")
c= ChuyenNganh("toan ung dung", "TM")



