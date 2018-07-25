import stdio

stdio.writeln('Tất cả các biển số đẹp để mang ra tổ chức đấu giá :')

#tim so doi xung

sodao=0
i=1000
# for i in range(i, 100000):
temp=i
while temp>0:
	sodao= sodao*10 + temp%10
	temp=temp//10
if i==sodao:
	#kiem tra tinh nguyen to
	for k in range(2,i):
		if (i%k==0): break
	else:

		stdio.write('   %d' %i)
			
	sodao=0
stdio.writeln('')	
	
	
	
