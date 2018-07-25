import sys
import stdio

N = float(sys.argv[1])

if N % 3 ==0:
	stdio.writeln(str(N) + ' chia het cho 3')
else :
	stdio.writeln(str(N) + ' khong chia het cho 3')
