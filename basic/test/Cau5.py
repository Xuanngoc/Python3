n= int(input())
m=input()
x=m.split()
total=0
for i in x:
    total+=float(i)
temp=total/n
count=0

for i in x:
    if float(i) > temp:
        count+=1 
print(count)           

