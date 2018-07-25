import stdio
import sys
import math

n=stdio.readInt()

max=0
for i in range(2, n+1):
	for k in range(2, i):
			if i%k==0:
				break
	else:
		if i>max:
			max=i
print(max)
			
