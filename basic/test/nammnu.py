import stdio
import sys


n=int(input())

a=list(n*"0")



count=0
for k in range(1, (2**n) ):
	check = 1
	for i in range (len(a)-1,-1,-1):
		if (a[i] == "0"):
			a[i] = "1"
			check = 0
			break
		else:
			a[i] = '0'
	binary = ''.join(a)
	flag=1
	for i in range(0, len(binary)-1):
		if binary[i] == "1" and binary[i]==binary[i+1]:
			flag=0
			count+=0
	if flag==1:
		count+=1
		print(binary)
print(count)
	
	
	



		
