import stdio
import sys

a = int(sys.argv[1])

sum=0

n1=1
n2=2
i=3
while i<=a:
	n=n1+n2
		

	# if n%2==0:
		# sum=sum+n
	n1=n2
	n2=n
	i=i+1

print(n)


