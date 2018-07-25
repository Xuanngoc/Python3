from stdio import *

a=readString()
b=readString()

x=len(a)
y=len(b)
count=0

for i in range(0, x):
    for k in range (0, y):
        if a[i]==b[k]:
            count+=1
writeln(count)            