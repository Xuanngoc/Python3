def perm(num1, num2):
    a=list(str(num1))
    b=list(str(num2))

    for i in a:
        if i in b:
            f=1
        else:
            return False
            break
    if f==1 and len(a)==len(b):
        return True
n=int(input("nhap so can kiem tra : "))

temp=n
x=1
count=0
for i in range(1, len(str(n))+1):
    x*=i
while count<x:
    
    if perm(n,temp ):
        print(temp)
        count+=1
    temp+=1    
        