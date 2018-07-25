import stdio
import sys

ngay = int(sys.argv[1])
thang = int(sys.argv[2])
nam = int(sys.argv[3])
x= ngay + 1

if x == 32:
	stdio.writeln('1')



#print(x , thang nam) 

# x=['','31', '28', '31', '30', '31', '30', 
#    '31', '31', '30', '31', '30', '31']

# if thang == 2:
# 	if (nam % 4==0 and (nam % 100 != 0 or nam % 400==0)):
# 	 	stdio.writeln('29')
# 	else:
# 		stdio.writeln('28')
# else:    	
# 	stdio.writeln(x[thang])