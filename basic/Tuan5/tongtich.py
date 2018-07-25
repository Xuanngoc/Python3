import stdio
import sys

n=int(sys.argv[1])

tong=0
tich=1	
for k in range(1, n+1):
	tich=tich*k
	tong=tong+tich	 
print(tong)	