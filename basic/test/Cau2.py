n=input()
from math import sqrt
x=n.split( )
a=int(x[0])
b=int(x[1])
c=int(x[2])

if a+b < c or a+c < b or b+c <a or c+a < b :
    print("-1")
else:
    #p =(a+b+c)/2
    #S=sqrt( p *(p-a)*(p-b)*(p-c))

    print(a+b+c)   
    
    