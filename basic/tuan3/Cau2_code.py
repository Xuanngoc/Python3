import stdio
import sys

thang = int(sys.argv[1])
nam = int(sys.argv[2])

x=['','31', '28', '31', '30', '31', '30', 
   '31', '31', '30', '31', '30', '31']

if thang == 2:
	if (nam % 4==0 and (nam % 100 != 0 or nam % 400==0)):
	 	stdio.writeln('29')
	else:
		stdio.writeln('28')
else:    	
	stdio.writeln(x[thang])