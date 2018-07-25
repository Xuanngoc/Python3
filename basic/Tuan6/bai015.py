import stdio
import math

n=stdio.readInt()

maxy=0
prime=True
for i in range(2, n+1):
	for k in range(2, n):
		if i % k ==0:
			prime=False
			break
		else:
			print(i)
# 			if n % i ==0 and i > maxy:
# 				maxy=i
				


# stdio.writeln(maxy)

