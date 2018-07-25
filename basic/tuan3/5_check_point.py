import stdio
import sys
import math


x1 = int(sys.argv[1])
y1 = int(sys.argv[2])
x2 = int(sys.argv[3])
y2 = int(sys.argv[4])

OP1 = math.sqrt((x1-0)**2 + (y1-0)**2)
OP2 = math.sqrt((x2-0)**2 + (y2-0)**2)

if OP1 == OP2 :
	stdio.writeln('Point(%s, %s) va Point(%s, %s) co cung khoang cach toi goc toa do' %(x1, y1, x2, y2))
elif OP1 > OP2 :
	stdio.writeln('Point(%s, %s) cach xa goc toa do hon Point(%s, %s)' %(x1, y1, x2, y2))
else:
	stdio.writeln('point(%s, %s) xa goc toa do hon Point(%s, %s)' %(x2, y2, x1, y2))
