# import stdio

n=int(input())
#theo quy tac cong nhi phan:
if n%10==0:

	N=n+1
	print(N)

else:
	a=(str(n))
	b=int(len(a))

	sum=0
# print(a[b-1])

	for i in range(1, b+1):
		sum=sum + int(a[b-i]) *(2**(b-i))
	sum=sum+1
	
	count=0
	x2=0
	while sum>0:
		a=sum%2
		count=count+1
		x1=a*(10**(count-1))
		x2=x2+x1
		sum=sum//2
	print(x2)

	

