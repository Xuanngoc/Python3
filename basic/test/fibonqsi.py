n=int(input())
f1=1
f2=1
fn=0
for i in range (3,n+1):
	fn=f1+f2
	f1= f2
	f2= fn
	print(fn)