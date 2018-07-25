import stdio

import math

n=stdio.readInt()

for i in range(n, 1, -1):
	a=int(math.sqrt(i))
	for k in range(2, a+1):
		if i%k == 0:
			break
	else:
		print(i)
		break

			
