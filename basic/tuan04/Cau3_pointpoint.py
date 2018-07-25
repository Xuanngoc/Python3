import stdio
import sys
import math

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
xc = float(sys.argv[3])
yc = float(sys.argv[4])
r = float(sys.argv[5])

OP = math.sqrt((x1-xc)**2 + (y1-yc)**2) 

if OP == r :
	stdio.writeln('Point(%s, %s) nam tren duong tron tam(%s, %s) ban kinh %s' % (x1, y1, xc, yc, r))
elif OP < r :
	stdio.writeln('Point(%s, %s) nam trong duong tran tam (%s, %s) ban kinh %s'  %(x1, y1, xc, yc, r))
else :
	stdio.writeln('Point(%s,%s) nam ngoai duong tron tam (%s, %s) ban kinh %s' %(x1, y1, xc, yc, r))