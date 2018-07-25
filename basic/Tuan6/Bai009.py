import stdio
import sys

n=int(sys.argv[1])

for i in range(2, n):
	if n % i==0:
		stdio.writeln('0')
		break
else:
	stdio.writeln('1')
