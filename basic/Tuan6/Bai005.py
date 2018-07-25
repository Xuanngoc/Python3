import stdio
import sys

N=int(sys.argv[1])

if N<999 or N>10000:
	stdio.writeln('-1')
else:
	sdx=0
	temp=N

	while temp>0:
		sdx=sdx*10 + temp%10
		temp=temp//10
	if sdx==N:
		stdio.writeln('DX')
	else:
		stdio.writeln('KDX')
				