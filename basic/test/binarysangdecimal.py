n=(input())
a=list(n) 
x=len(a)

sum1=0
temp=0
for i in range(x-1, -1, -1):

    sum1 =sum1 +int(a[temp]) * (2**(i))
    temp+=1
    # print(int(a[temp]) * (2**(i)))
print("sum1= ", sum1)
    