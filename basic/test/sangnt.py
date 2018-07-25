from math import*

N=int(input())

sequence =  [ True ] * (N+1)

for p in range(2, int(sqrt(N))+1):
    if not sequence[p]:
    for n in range(p*p, N+1, p):
        sequence[n] = False
for i in range(2, N+1):
    if sequence[i]:
        print(i, end=" ") 
print("")               