import stdio
import sys

N=int(sys.argv[1])

if N<1000 or N>10000:
	stdio.writeln('-1')
else:
	a=N%10
	b=N%100//10
	c=N%1000/100
	d=N//1000
mx=max(a,b ,c, d)
stdio.writeln(mx)   