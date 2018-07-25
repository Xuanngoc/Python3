def prime(n):
	for i in range(2, n):
		flag=1
		if n%i==0:
			flag=0
			break
	if flag==1:
		return n		
	else:
		return("not")
n=int(input('nhap n'))
print(prime(n))
