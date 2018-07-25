import stdio
import sys

a=float(sys.argv[1])
b= float(sys.argv[2])
c= float(sys.argv[3])
d= float(sys.argv[4])

TBc=(a*2 + b +c*2 + d)/6
if TBc >=9 :
	if a>6.5 and b>6.5 and c>6.5 and d >6.5 :
		stdio.writeln('SX')
	else:
		stdio.writeln('G')
elif TBc>=8:
	if a>= 5 and b>=5 and c>=5 and d >=5 :
		stdio.writeln('G')
	else:
		stdio.writeln('K')
elif TBc>=6.5:
	if a>=3 and b>=3 and c>= 3 and d >=3 :
		stdio.writeln('K')
	else:
		stdio.writeln('TB')
elif TBc>=5:
	if a>=2 and b>=2 and c>=2 and d >=2:			
		stdio.writeln('TB')
	else:
		stdio.writeln('Y')
else:
	stdio.writeln('Y')			
