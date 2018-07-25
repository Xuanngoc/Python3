import stdio

n=stdio.readInt()

a=n
while a>1:
	flag=1
	for i in range(2, a):
		if a%i==0:
			flag=0
			break
	if flag==1:
		print(a)
		break		
	a=a-1

