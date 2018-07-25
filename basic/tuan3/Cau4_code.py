import stdio
import math
import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a + b <= c or a + c <= b or b + c <= a :
	stdio.writeln('Khong phai la tam giac')
else:
	if a**2 == b**2 + c**2 or b**2==a**2 + c**2 or c**2 == a**2 + b**2 : 
		stdio.writeln('Tam giac vuong')
	elif a==b==c :
		stdio.writeln('Tam giac deu')
	else:
		stdio.writeln('Tam giac binh thuong')

	p = ((a+b+c)/2)
	S = (math.sqrt(p*(p-a)*(p-b)*(p-c)))
	stdio.writeln('dien tich tam giac: %s ' % S )			
