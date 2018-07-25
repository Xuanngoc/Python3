import stdio


n=str(input("nhap n: "))
a=len(n)
max=0
for i in range(0, a ):
	if int(n[i]) > max:
		max=int(n[i])
print(max)		