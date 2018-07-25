n=int(input())
m=int(input())

from math import sqrt

prime=[True] * (m+1)
total=0
for p in range(n, int(sqrt(m))+1):
    for k in range(p*p, m+1, p):
        if prime[p]:
            prime[k]=False
for p in range(n, m+1):
    if prime[p]:
        total+=p
print(total)                    