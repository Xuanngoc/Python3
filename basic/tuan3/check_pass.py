import stdio
import sys

D1 = float(sys.argv[1])
D2 = float(sys.argv[2])
D3 = float(sys.argv[3])

if D1<=1.5 or D2<=1.5 or D3<=1.5 :
	stdio.writeln('Bi diem liet - KHONG DO DAI HOC')
elif  D1 + D2 + D3 < 16:
	stdio.writeln('Khong du diem do dai hoc')
else:
	stdio.writeln('Congratulate - Do dai hoc')		 
