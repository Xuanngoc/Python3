import sys
import math

def isPrime(n:int):
	if n == 2:
		return True
	for i in range(2,int(math.sqrt(n)+1)):
		if n % i == 0:
			return False
	return True

n = int(sys.argv[1])

index = 0
i = 2

while index < n:
	if (isPrime(i)):
		index +=1
	i +=1
	
print ("Số nguyên tố thứ ",n," là ",i-1)