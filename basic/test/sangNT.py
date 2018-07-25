import math

n=int(input())

x=[True] * (n + 1)

for p in range (2, int(math.sqrt(n)) + 1 ):
	for k in range (p*p , n + 1, p):
		if x[p] == True:
			x[k] = False
for p in range (2, n + 1):
	if x[p] == True:
		print( p, end='   ')
