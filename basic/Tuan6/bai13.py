import stdio

n=stdio.readInt()

maxy=0
for i in range(n, 0, -1):
	# print(i)
	#kiem tra tinh hoan hao
	sum=0
	for k in range(1, i):
		if i%k==0:
			# print('k'+str(k))
			sum=sum+k
				
	if sum==i:
		print(i)
		break
	# if sum==k:
		# print(i) 
				
			






