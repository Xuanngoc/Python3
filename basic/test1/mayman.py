n=int(input("nhap ve co : "))
a=[]

dem=0	
k=0
while True:
		k+=1




		if k <10:
			dem+=1
		elif int(len(str(k)))==2:
			if k%11==0:
				dem+=1
		elif int(len(str(k)))==3:
			if k%111==0:
				dem+=1
		elif int(len(str(k)))==4:
			if k%1111==0:
				dem+=1
		elif int(len(str(k)))==5:
			if k%11111==0:
				dem+=1
		elif int(len(str(k)))==6:
			if k%111111==0:
				dem+=1
		elif int(len(str(k)))==7:
			if k&1111111==0:
				dem+=1
		elif int(len(str(k)))==8:
			if k%11111111==0:
				dem+=1
		elif int(len(str(k)))==9:
			if k%111111111==0:
				dem+=1

		if k==n:
			break
print(dem)					
