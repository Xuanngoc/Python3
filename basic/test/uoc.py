n=int(input("nhap n :"))
m=int(input("nhap m :"))


sum1=0
sum=0
for i in range(1, n):
	if n%i==0:
		sum+=i
for k in range(1, m):
	if m%k==0:
		sum1+=k	
if m==sum and n==sum1:

	print(str(sum)+ " " + str(sum1))			