from math import sqrt

m=int(input())
def sangnt(n):
    prime=[True] *(n+1)
    prime[0]=prime[1]=False
    prime1=[]
    for p in range(2, int(sqrt(n))+1):
        for k in range(p*p, n+1, p):
            if prime[p]:
                prime[k]=False
    for p in range(1, n+1):
        if prime[p]:
            prime1.append(p)
    return prime1

print((sangnt(200000)[m-1]))                   