
sodao=0

#tim so doi xung
for i in range(1000, 100000):
	tam=i
	while tam>0:
		sodao= sodao*10 + tam%10
		tam=tam//10
	if i==sodao:
		print('So %d la do doi xung' %i)
	sodao=0
	
	
