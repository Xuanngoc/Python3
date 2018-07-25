def fac(n):
	if n<=1:
		return 1
	if n==2:
		return 2
	else:
		return n*fac(n-1)

n=int(input("nhap n : "))				
print(fac(n))
