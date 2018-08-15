from Sinhvien import *
from Khoa import *


def main():
    DSSinhVien = []
    DSChuyenNghanh = []
    DSKhoa = []
    print("Cac thao tac: ")
    print("\tA. Them, sua, xoa, hien thi thong tin sinh vien")
    print("\tB. Them, sua, xoa, hien thi thon tin cac khoa")
    print("\tC. Them, sua, xoa, hien thi thong tin cac chuyen nghanh")
    print("\tD. Tim kiem sinh vien theo ma sinh vien")
    print("\tE. Sap xep sinh vien theo ma sinh vien tu thap toi cao\n")
    thaoTac = input("\nNhap thao tac ban muon(A, B, C, D, E, O): ")

    if thaoTac == "A":
        while True:
            print("Cac thao tac voi sinh vien:")
            print("\t1. Them sinh vien.")
            print("\t2.Sua thong tin sinh vien")
            print("\t3.Xoa thong tin sinh vien")
            print("\t4.Hien thi thong tin sinh vien\n\t5.Done\n")
            choose = input("Nhap lua chon: ")
            if(choose == "1"):
                DSSinhVien.append(SinhVien.ThemSV())
                print("\nThao tac thanh cong.\n\n")
            elif(choose == "2"):
                print("nhap ma sinh vien ban muon sua: ")
                tempMaSV = input()
                for i in DSSinhVien:
                    if i.getMaSV() == tempMaSV:
                        i.SuaTT()
                        print("\nThao tac thanh cong.\n\n")
                        break
            elif choose == "3":
                print("nhap ma sinh vien ban muon xoa: ")
                tempMaSV = input()
                for i in DSSinhVien:
                    if i.getMaSV() == tempMaSV:
                        del i
                        print("\nThao tac thanh cong.\n\n")
                        break
            elif choose == "4":
                tempMaSV = input("Nhap ma sinh vien ban muon hien thi: ")
                for i in DSSinhVien:
                    if i.getMaSV() == tempMaSV:
                        print(i)
                        break
            else:
                break
    elif thaoTac == "B":
        while True:
            print("Cac thao tac voi chuyen nghanh:")
            print("\t1.Them chuyen nganh\n\t2.Sua chuyen nganh")
            print("\t3.Xoa chuyen nghanh")
            print("\t4.Hien thi thong tin chuyen nganh\n")
            choose = input("Nhap lua chon: ")
            if choose == "1":
                DSChuyenNghanh.append(ChuyenNganh.ThemChuyenNghanh())
                print("\nThao tac thanh cong.\n\n")
            elif choose == "2":
                temp = input("Nhap ma chuyen nghanh ban muon thay doi: ")
                for i in DSChuyenNghanh:
                    if i.getMaChuyenNganh() == temp:
                        i.SuaTT()
                        print("\nThao tac thanh cong.\n\n")
                        break
            elif choose == "3":
                temp = input("Nhap ma chuyen nghanh ban muon xoa: ")
                for i in DSChuyenNghanh:
                    if i.getMaChuyenNganh == temp:
                        del i
                        print("\nThao tac thanh cong.\n\n")
                        break
            elif choose == "4":
                temp = input("Nhap ma chuyen nghanh ban muon hien thi: ")
                for i in DSChuyenNghanh:
                    if i.getMaChuyenNganh == temp:
                        print(i)
                        break
            else:
                break

    elif thaoTac == "C":
        while True:
            print("Cac thao tac voi khoa:")
            print("\t1.Them khoa\n\t2.Sua thong tin khoa")
            print("\t3.Xoa khoa")
            print("\t4.Hien thi thong tin khoa\n")
            choose = input("Nhap lua chon: ")
            if choose == 1:
                DSKhoa.append(Khoa.)


        
if __name__ == "__main__":
    main()
