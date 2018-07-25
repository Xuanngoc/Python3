import stdio

import math

n=stdio.readInt()
max=0
for i in range(n, 1, -1):
	a=int(math.sqrt(i))
	for k in range(2, a+1):
		if i%k == 0:
			break
	else:
		if i>max:
			max=i
print(max)
			
