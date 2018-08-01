class ChuyenNganh:
    __tenChuyenNganh = None
    __maChuyenNganh = None
    
    def __init__(self, a, b):
        self.__tenChuyenNganh =a
        self.__maChuyenNganh= b

    def __del__(self):
        del self.__tenChuyenNganh, self.__maChuyenNganh

    def __str__(self):
        return ("Ten chuyen nganh: %s\nMa chuyen nganh: %s" %(self.__tenChuyenNganh, self.__maChuyenNganh))

    #setters
    def setTenChuyenNganh(self, a):
        self.__tenChuyenNganh =a
    def setMaChuyenNganh(self, a):
        self.__maChuyenNganh =a
    #getters
    def getTenChuyenNganh(self):
        return self.__tenChuyenNganh
    def getMaChuyenNganh(self):
        return self.__maChuyenNganh
    
    #create
    def ThemSV():
        return ChuyenNganh(input(), input())


