import stdio
import math
n=stdio.readInt()
sum=0
temp=2
while True:
	flag=1
	for i in range(2, int(math.sqrt(temp)+1)):
		if temp%i==0: 
			flag=0
			break
	if flag==1:
		sum+=1		
	if sum==n:
		print(temp)
		break
	temp+=1		