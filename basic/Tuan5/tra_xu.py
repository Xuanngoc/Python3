import sys
i=0
k=0
j=0
n=int(sys.argv[1])
for a in range (1, n+1):
	while n>=5:
		i=n//5
		n=n-5*i
		if n==0:
			break
		# print(i)
		if n<5:
			while n>=2:
				j=n//2
				n=n-2*j
				if n==0:
					break
				# print(j)
				if n<2:
					while n>=1:
						k=n//1
						n=n-k*1
						# print(k)
x=i+j+k

print('Tra it nhat %d dong ' %x)
print(i*str(5) + j*str(2) + k*str(1) )


