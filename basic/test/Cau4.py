n=int(input())

while True:
    n+=1
    for i in range(2, n):
        if n%i==0:
            f=1
            break
        else:
            f=2
    if f!= 1:
        print(n)           
        break