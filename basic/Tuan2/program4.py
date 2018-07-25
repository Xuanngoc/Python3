import stdio
import math
import sys

x = float (sys.argv[1])
kq = 3*math.sin(x/2)**2*math.cos(3*math.pi/2 +x/2)+ 3*math.sin(x/2)**2*math.cos(x/2)
stdio.writeln( kq )