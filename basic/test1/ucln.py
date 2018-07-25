
n=int(input("nhap n : "))
m=int(input("nhap m : "))


if m==n:
	print(m)
else:	
	while n!=m:
		if n>m:
			n-=m
		else:
			m-=n
print(m,n)
			
