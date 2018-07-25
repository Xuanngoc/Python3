import stdio
import math

n=stdio.readInt()

count=1  


for i in range(3, 15):
	a=int(math.sqrt(i))
	for k in range(2, a+1):
		if i%k==0:
			break
	else:
		count=count+1
		# print(i)
		# print('-%d' %count)
		if count==n:
			print(i)


