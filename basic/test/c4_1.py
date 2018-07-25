import stdio
import sys

# n=stdio.readInt()
dodainhiphan = stdio.readInt()

a = list(dodainhiphan* "0" )
stdio.write(str(dodainhiphan*'0'+ " "))
binary=""
# while b <= dodainhiphan:
for k in range(1, (2**dodainhiphan) ):
	check = 1
	for i in range (len(a)-1,-1,-1):
		if (a[i] == "0"):
			a[i] = "1"
			check = 0
			break
		else:
			a[i] = '0'
	binary = ''.join(a)

	# if check == 1:
	# 	binary = "1".join(a)
	print(binary, end=" ")
stdio.writeln("")	
	



		
