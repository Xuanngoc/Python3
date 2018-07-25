from math import sqrt

n=int(input())

prime=[True] *(n+1)
for p in range(2, int(sqrt(n))+1):
    for k in range(p*p, n+1, p):
        if prime[p]:
            prime[k]=False
for p in range(2, n+1):
    if prime[p]:
        print(p, end=" ")            
