n=input()
# m=input()

s=[]

a=len(n)
for i in range(0, a):
	for k in range(0,a):
		if n[i]==n[k]:
			
			s=(n.strip(n[i]))
			print(s)			
