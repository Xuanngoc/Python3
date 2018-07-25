import stdio
import math

n=stdio.readInt()

count=0

for i in range(1, n+1):
	if n % i:
		for i in range(2, int(math.sqrt(i))):
			if n % i==0:
				count+=1
	if count == 2:
		print(i)		