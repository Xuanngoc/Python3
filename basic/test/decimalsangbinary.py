n=int(input())
str1=""
while n>0:
    str1 = str(n%2) + str1
    n=n//2
print(str1)    