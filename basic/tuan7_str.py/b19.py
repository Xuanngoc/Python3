import stdio

str1 = stdio.readString()
str2 = stdio.readString()

if len(str1) > len(str2):
	a = str1
	b = str2
else:
	a = str2	
	b = str1
count = 0
length = len(b)

for i in range(0, len(a)):
	temp = a [ i : ( i + length )]
	if temp == b:
		count += 1	
stdio.writeln(str(count))		