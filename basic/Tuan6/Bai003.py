import stdio
import sys

a=int(sys.argv[1])
b=int(sys.argv[2])

k = a // b
r = a % b 
stdio.writeln(k)
stdio.writeln(r)