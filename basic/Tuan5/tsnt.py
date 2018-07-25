import stdio	
import sys

n= int(sys.argv[1])
i=2
while n!=1:
	if n%i==0:
		stdio.writeln(i)
		n=n/i
	else:
		i=i+1	
