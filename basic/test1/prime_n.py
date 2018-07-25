import stdio
import math

n=stdio.readInt()

temp=n

while True:
	temp+=1
	for i in range(2, int(math.sqrt(n)+1)):
		flag=1
		if temp%i==0:
			flag=0
			break
	if flag==1:
		print(temp)
		break		