import stdio
import sys

n=int(sys.argv[1])

sum=0
     
for i in range(1, n):
	if n % i==0:
		sum=sum+1
stdio.writeln(sum)		