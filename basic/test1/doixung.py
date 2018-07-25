import stdio

n=stdio.readInt()

a=n
doixung=0
while a>0:
	doixung=doixung*10 +a%10
	a=a//10
if doixung==n:

	print("ok")
else:
	print("not")		