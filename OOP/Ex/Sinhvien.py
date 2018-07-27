from abc import ABC, abstractmethod

class SinhVien(ABC):
    _maSV= 0
    _tenSV= None
    _maNganh= None
    _age= 0

    def __init__(self, a,b,c,d):
        self._maSV, self._tenSV, self._maNganh, self._age = a,b,c,d
    def __del__(self):
        del self._maSV, self._tenSV, self._maNganh, self._age

    #setters
    def setMaSV(self, a):
        self._maSV =a
    def setTenSV(self, a):
        self._tenSV =a
    def setMaNganh(self, a):
        self._maNganh =a
    def setAge(Self, a):
        self._age =a        

    #getters
    def getMaSV(self):
        return self._maSV
    def getTenSV(self):
        return self._tenSV
    def getMaNganh(self):
        return self._maNganh
    def getAge(self):
        return self._age

    #def __str__(self):
     #   return("Ma sinh vien: %d \nTen sinh vien: %s\nMa nganh: %s\nTuoi: %d" % (self._maSV, self._tenSV,self._maNganh, self._age))
class SinhVienDaiCuong(SinhVien):
    diemLyThuyetDaiCuong = 0
    diemThucHanhDaiCuong =0

    def __init__(self, maSV, Ten, maNganh, age, DLT, DTT):
        SinhVien.__init__(self,maSV, Ten, maNganh, age)
        self.diemLyThuyetDaiCuong=DLT
        self.diemThucHanhDaiCuong =DTT
    def __del__(self):
        SinhVien.__del__(self)
        del self.diemLyThuyetDaiCuong, self.diemThucHanhDaiCuong
    #setters
    def setDiemLyThuyetDaiCuong(self, a):
        self.diemLyThuyetDaiCuong =a
    def setDiemThucHanhDaiCuong(self, a):
        self.diemThucHanhDaiCuong =a

    #getters
    def getDiemLyThuyetDaiCuong(self):
        return self.diemLyThuyetDaiCuong
    def getDiemThucHanhDaiCuong(self):
        return self.diemThucHanhDaiCuong

    def __str__(self):
        return ("Ma sinh vien: %d \nTen sinh vien: %s\nMa nganh: %s\nTuoi: %d\nDiem ly thuyet dai cuong: %d\nDiem thuc hanh dai cuong: %d" %(self._maSV, self._tenSV,self._maNganh, self._age,self.diemLyThuyetDaiCuong, self.diemThucHanhDaiCuong))

class SinhVienChuyenNganh(SinhVien):
    diemLyThuyetChuyenNganh = 0
    diemThucHanhChuyenNganh =0

    def __init__(self, maSV, Ten, maNganh, age, DLT, DTT):
        SinhVien.__init__(self,maSV, Ten, maNganh, age)
        self.diemLyThuyetChuyenNganh=DLT
        self.diemThucHanhChuyenNganh =DTT
    def __del__(self):
        SinhVien.__del__(self)
        del self.diemLyThuyetChuyenNganh, self.diemThucHanhChuyenNganh
    #setters
    def setDiemLyThuyetChuyenNganh(self, a):
        self.diemLyThuyetChuyenNganh =a
    def setDiemThucHanhChuyenNganh(self, a):
        self.diemThucHanhChuyenNganh =a

    #getters
    def getDiemLyThuyetChuyenNganh(self):
        return self.diemLyThuyetChuyenNganh
    def getDiemThucHanhChuyenNganh(self):
        return self.diemThucHanhChuyenNganh

    def __str__(self):
        return ("Ma sinh vien: %d \nTen sinh vien: %s\nMa nganh: %s\nTuoi: %d\nDiem ly thuyet dai cuong: %d\nDiem thuc hanh dai cuong: %d" %(self._maSV, self._tenSV,self._maNganh, self._age,self.diemLyThuyetChuyenNganh, self.diemThucHanhChuyenNganh))

a = SinhVienChuyenNganh(1231, "Bui Ngoc", "TI", 18, 7, 8)

print(a)

