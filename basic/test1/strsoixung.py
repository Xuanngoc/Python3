
longstr=input("nhap xau : ")

for i in range(0, len(longstr)):
	for m in range(2, len(longstr)):
		str1=""
		for k in longstr[i : i+m]:
			str1+=k

		str2=""
		for l in range(len(str1)-1, -1, -1):
			str2+=str1[l]
		# print("str2", str2)	
		if str1 == str2 and len(str2)==m:
			
			f=1
			break
		else:
			
			f=2
			
	if f==1 :
		break		
if f==1:
	print("ok")			
if f==2:
	print("not")				