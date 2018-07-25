import stdio


n=int(input('nhap so '))
count=0
x2=0
while n>0:
	a=n%2
	count=count+1
	x1=a*(10**(count-1))
	x2=x2+x1
	n=n//2
	stdio.writeln(x2)
