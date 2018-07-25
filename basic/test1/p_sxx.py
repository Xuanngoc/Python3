n=int(input("nhap so ve ban co : "))
# print((len(str(n)))*'1')
sum1=0
while n>10:
	sum1+=n//int(len(str(n))*"1")
	n=n//10
	if n<10:
		sum1+=n
print(sum1)
