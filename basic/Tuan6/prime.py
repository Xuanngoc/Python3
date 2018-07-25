import stdio
import math

n=stdio.readInt()
dem=0
for i in range(1, n+1):
	if n%i==0:
		dem += 1
if dem==2:
	stdio.writeln('Is prime')
else:
	stdio.writeln('Is not prime ')			