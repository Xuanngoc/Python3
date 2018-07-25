import stdio
import sys
n=int(sys.argv[1])


sum=0

for i in range(1, n):
	
	
	if n%i==0:
		sum=sum+i

	

if sum == n :
	stdio.writeln('1')
else:
	stdio.writeln('0')		

		
