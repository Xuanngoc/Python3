import stdio
import math

n=stdio.readInt()

if n == 1:
	print('2')
else:
	count=1  
	temp = 2
	while True:
		temp += 1
		a=int(math.sqrt(temp))
		for k in range(2, a+1):
			if temp%k==0:
				break
		else:
			# print(temp)
			count=count+1
			if count==n:
				print(temp)
				break


