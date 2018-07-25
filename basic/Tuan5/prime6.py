print('Tất cả các biển số đẹp để mang ra tổ chức đấu giá :')


#tim so doi xung

sodao=0
for i in range(1000, 100000):
	tam=i
	while tam>0:
		sodao= sodao*10 + tam%10
		tam=tam//10
	if i==sodao:
		#kiem tra tinh nguyen to
		for k in range(2,i):
  			if (i%k==0): break
		else:

			print(i)
	sodao=0
	
	
