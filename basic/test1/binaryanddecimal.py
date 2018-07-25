def doixung(num1):
    temp=num1
    a=0
    while temp>0:
        a=a*10 + temp % 10
        temp=temp//10
    if num1 == a:
        return True
def binary(num1):
    b=""
    b=num1%2
    num1//2


n=int(input())



