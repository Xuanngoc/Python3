import stdio
import math

n=stdio.readInt()
maxy=0

for i in range(1, n+1):
	a=math.floor(math.sqrt(i))
	b=math.ceil(math.sqrt(i))
	if a==b and i>maxy:
		maxy=i
stdio.writeln(maxy)		