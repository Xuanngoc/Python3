import sys
import stdio


stdio.writeln("Nhap so muon tinh :  ")
n= stdio.readInt()

fac=1

for i in range(1, n+1):
	fac = fac *i

stdio.writeln(str(fac))