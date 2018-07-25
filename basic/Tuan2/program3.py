
import stdio
import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = math.sqrt(2*a**(b+min(3,a))+6*b**(a-max(0,b)))/abs(a**2 - b**(2**3))

stdio.writeln('BXK3CS100 =' + str(c))

