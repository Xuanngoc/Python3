
class SinhVien():
    def __init__(self, maSV, tenSV, maNganh, tuoi):
        self.__maSV = maSV
        self.__tenSV = tenSV
        self.__maNganh = maNganh
        self.__tuoi = tuoi

    def __del__(self):
        del self.__maSV, self.__tenSV, self.__maNganh, self.__tuoi

    def ThemSV():
        return SinhVien(input("Nhap ma sinh vien: "), input("Nhap ten sinh vien: "), input("Nhap ma nganh: "), input("Nhap tuoi: "))

    def SuaTT(self):
        print("Sua thong tin sinh vien: % s" % self.__maSV)
        while True:
            print("1.Ten sinh vien\n2.Ma nganh hoc\n3.Tuoi\n4.exit")
            choose = input()
            if choose == "1":
                self.__tenSV = input("Nhap ten moi cho: %s " % self.__tenSV)
            elif choose == "2":
                self.__maNganh = input("Nhap ma nganh hoc moi : ")
            elif choose == "3":
                self.__tuoi = int(input("Nhap tuoi moi: "))
            else:
                break
        print("Thong tin sau khi sua: ")
        print(self)

    # setters
    def setMaSV(self, maSV):
        self.__maSV = maSV

    def setTenSV(self, tenSV):
        self.__tenSV = tenSV

    def setMaNganh(self, maNganh):
        self.__maNganh = maNganh

    def setAge(self, tuoi):
        self.__tuoi = tuoi

    # getters
    def getMaSV(self):
        return self.__maSV

    def getTenSV(self):
        return self.__tenSV

    def getMaNganh(self):
        return self.__maNganh

    def getAge(self):
        return self.__age

    def __str__(self):
        return("Ma sinh vien: %s \nTen sinh vien: %s\nMa nganh: %s\nTuoi: \
            %s" % (self.__maSV, self.__tenSV, self.__maNganh, self.__tuoi))

# class Sinh vien dai cuong
class SinhVienDaiCuong(SinhVien):
    def __init__(self, maSV, Ten, maNganh, age, diemLyThuyet, diemThucHanh):
        SinhVien.__init__(self, maSV, Ten, maNganh, age)
        self.__diemLyThuyetDaiCuong = diemLyThuyet
        self.__diemThucHanhDaiCuong = diemThucHanh

    def __del__(self):
        SinhVien.__del__(self)
        del self.__diemLyThuyetDaiCuong, self.__diemThucHanhDaiCuong

    def SuaTT(self):
        SinhVien.SuaTT(self)

    # setters
    def setDiemLyThuyetDaiCuong(self, diemLyThuyet):
        self.__diemLyThuyetDaiCuong = diemLyThuyet

    def setDiemThucHanhDaiCuong(self, diemThucHanh):
        self.__diemThucHanhDaiCuong = diemThucHanh

    # getters
    def getDiemLyThuyetDaiCuong(self):
        return self.__diemLyThuyetDaiCuong

    def getDiemThucHanhDaiCuong(self):
        return self.__diemThucHanhDaiCuong

    def __str__(self):
        print(super())
        return ("Diem ly thuyet dai cuong: % s\nDiem thuc hanh dai cuong: \
        % s" % (self.__diemLyThuyetDaiCuong, self.__diemThucHanhDaiCuong))

class SinhVienChuyenNganh(SinhVien):

    def __init__(self, maSV, Ten, maNganh, age, diemLyThuyet, diemThucHanh):
        SinhVien.__init__(self, maSV, Ten, maNganh, age)
        self.__diemLyThuyetChuyenNganh = diemLyThuyet
        self.__diemThucHanhChuyenNganh = diemThucHanh

    def __del__(self):
        SinhVien.__del__(self)
        del self.__diemLyThuyetChuyenNganh, self.__diemThucHanhChuyenNganh

    # setters
    def setDiemLyThuyetChuyenNganh(self, diemLyThuyet):
        self.diemLyThuyetChuyenNganh = diemLyThuyet

    def setDiemThucHanhChuyenNganh(self, diemThucHanh):
        self.diemThucHanhChuyenNganh = diemThucHanh

    # getters
    def getDiemLyThuyetChuyenNganh(self):
        return self.diemLyThuyetChuyenNganh

    def getDiemThucHanhChuyenNganh(self):
        return self.diemThucHanhChuyenNganh

    def __str__(self):
        return ("Ma sinh vien: %d \nTen sinh vien: %s\nMa nganh: %s\nTuoi:\
        %d\nDiem ly thuyet dai cuong: %d\nDiem thuc hanh dai cuong: %d\
        " % (self._maSV, self._tenSV, self._maNganh, self._age, self.diemLyThuyetChuyenNganh, self.diemThucHanhChuyenNganh))
