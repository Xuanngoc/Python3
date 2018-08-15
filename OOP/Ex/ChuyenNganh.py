class ChuyenNganh:
    __tenChuyenNganh = None
    __maChuyenNganh = None

    def __init__(self, tenChuyenNganh, maChuyenNganh):
        self.__tenChuyenNganh = tenChuyenNganh
        self.__maChuyenNganh = maChuyenNganh

    def __del__(self):
        del self.__tenChuyenNganh, self.__maChuyenNganh

    def __str__(self):
        return ("Ten chuyen nganh: %s\nMa chuyen nganh: %s" % (self.__tenChuyenNganh, self.__maChuyenNganh))

    # setters
    def setTenChuyenNganh(self, tenChuyenNganh):
        self.__tenChuyenNganh = tenChuyenNganh

    def setMaChuyenNganh(self, maChuyenNganh):
        self.__maChuyenNganh = maChuyenNganh

    # getters
    def getTenChuyenNganh(self):
        return self.__tenChuyenNganh

    def getMaChuyenNganh(self):
        return self.__maChuyenNganh

    # 
    def ThemChuyenNghanh():
        return ChuyenNganh(input("Nhập tên chuyên ngành: "), input("Nhập ma chuyên ngành: "))
    def SuaTT(self):
        print("Sua thong tin nghanh: % s" % self.getTenChuyenNganh())
        print("1.Sua ten chuyen nganh\n2.Sua ma chuyen nghanh\n3.Done")
        choose = input("Chon thao tac(1, 2): ")
        while True:
            if choose == "1":
                self.__tenChuyenNganh = input("Nhap ten chuyen nganh moi: ")
                break
            elif choose == "2":
                self.__maChuyenNganh = input("Nhap ma chuyen nganh moi: ")
                break
            else:
                break;
        print("Thong tin sau khi sua\n% s:" % self)


