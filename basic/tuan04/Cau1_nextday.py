import stdio
import sys
day = int(sys.argv[1])
month = int(sys.argv[2])
year = int(sys.argv[3])





if month ==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
	day = day +1
	if day== 32:
		month = month + 1
		# stdio.writeln('1/%d/%d' %(month, year))
		if month==13:
			year = year+1
			month = 1
			stdio.writeln('1/%d/%d' %(month,year))
		else:
			day =1
			stdio.writeln('%d/%d/%d' %(day, month, year))	

	else:
		stdio.writeln('%d/%d/%d' %(day,month,year))	

elif month==4 or month ==6 or month==9 or month== 11:
	day = day + 1
	if day == 31:
		month = month +1
		stdio.write('1/%d/%d' %(month, year))	
	else:
		stdio.writeln('%d/%d/%d' %(day, month, year))	
elif month == 2:
 	if (year % 4==0 and (year % 100 !=0 or year % 400==0)):
 		if day ==29:
 			day ==day +1
 			stdio.write('1/3/%d' % year)
 		else:
 			day = day+1
 			stdio.writeln('%d/%d/%d' %(day, month, year))	
 	else:
 		day = day +1
 		if day == 29:
 			stdio.writeln('1/3/%d' % year)
 		else:
 			stdio.writeln('%d/%d/%d' %(day, month, year))	
