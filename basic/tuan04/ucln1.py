import stdio

num1=stdio.readInt()
num2=stdio.readInt()

while num1!=num2:
	if num1>num2:
		num1=num1-num2
	else:
		num2=num2-num1	
print(num1)		