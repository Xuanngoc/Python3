import stdio

a=stdio.readString()
b=stdio.readString()

lena=len(a)
lenb=len(b)

count = 0
for i in range (0,lenb-lena+1):
	if (b[i:i+lena]==a):
		count = count + 1
print (count)			