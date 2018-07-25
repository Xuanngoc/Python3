import stdio
import sys

a= int(sys.argv[1])
b= int(sys.argv[2])
c= int(sys.argv[3])

max=a
if b > max:
	max=b
	
if c > max:
	max=c
stdio.writeln(str(max) )	
