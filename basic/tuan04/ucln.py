import stdio


num1=stdio.readInt()
num2=stdio.readInt()

while num2>0:
	tam=num2
	num2=num1%num2
	num1=tam
stdio.writeln(str(num1)	)
