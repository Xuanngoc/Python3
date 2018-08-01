from Sinhvien import *
from Khoa import *

if __name__ == "__main__":
    DSSV =[]
    while True:
        print("1. Them sinh vien.\n2.Sua thong tin sinh vien\n3.Xoa thong tin sinh vien\
        4.Hien thi thong tin sinh vien")
        print("Nhap lua chon: ")
        choose = input()
        if(choose == "1"):
            DSSV.append(SinhVien.input())
        if(choose == "2"):
            print("nhap ma sinh vien ban muon sua: ")
                

