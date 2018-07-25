import stdio

stdio.writeln('nhap so = ')
so_input=stdio.readInt()

sodao=0
tam=so_input

while tam>0:
	
	sodao= sodao*10 + tam%10
	tam=tam//10
		
if so_input==sodao:
	stdio.writeln('%d la do doi xung' %so_input)
else:
	stdio.writeln('%d khong phai la so doi xung' %so_input)	