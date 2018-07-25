import stdio
import sys

a=stdio.readString()
b=stdio.readString()

x=len(a)
y=len(b)

if x>y:
	b='0' * (x-y) + b
else:
	a='0' * (y-x) + a	

c=""	
nho=0
dem=0
for i in range(x-1, -1, -1):
	d=int(a[i] + int(b[i]) + nho
	if d > 10:
		kq = c + str(d % 10)	
		nho=1
		dem+=1
	else:
		total = c + str(d%10)
print(total)				