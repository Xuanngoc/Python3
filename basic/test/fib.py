def fac(i):
	if i <= 1:
		return 1
	return i * fac(i-1)	
print(fac(6))