b1=input()
b2=input()

if len(b1) > len(b2):
    x=len(b1)-len(b2)
    b2=x*"0" +b2
    
else:
    x=len(b2)-len(b1)
    b1=x*"0" + b1
str1=""
nho=0
for i in range(len(b1)-1, -1, -1):
    b=int(b1[i]) +int(b2[i]) + nho
    
    if b ==1:
        str1="1" + str1
        
    if b>2:
        str1="1" + str1
        nho=1
    if b==2:
        str1="0" + str1
        nho=1
    if b==0:
        str1="0" + str1
if nho==1:       
    str1=str(nho) +str1    
print(str1)                   

       

