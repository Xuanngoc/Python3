import stdio
import math

n=stdio.readInt()



prime=True
maxy=0

for i in range(n, 0, -1):
	if n % i == 0:
		
		for k in range(2, int(math.sqrt(i))+1):
			if i%k==0:
				# print(i)
				break
		else:
			print(i)
			break		

		
			

			
		 	


