import stdio
import sys
import math


#phep cong +
stdio.write(sys.argv[1] + '+' + sys.argv[2] + '=')
stdio.writeln(int(sys.argv[1]) + int(sys.argv[2]))

#phep tru -
stdio.write(sys.argv[1] + '-' + sys.argv[2] + '=')
stdio.writeln(int(sys.argv[1]) - int(sys.argv[2]))

#phep nhan *
stdio.write(sys.argv[1] + '*' + sys.argv[2] + '=')
stdio.writeln(int(sys.argv[1]) * int(sys.argv[2]))

#phep chia
stdio.write(sys.argv[1] + '/' + sys.argv[2] + '=')
stdio.writeln(int(sys.argv[1]) / int(sys.argv[2]))

#phep chia lay nguyen
stdio.write(sys.argv[1] + '//' + sys.argv[2] + '=')
stdio.writeln(int(sys.argv[1]) // int(sys.argv[2]))

#phep chia lay du
stdio.write(sys.argv[1] + '%' + sys.argv[2] + '=')
stdio.writeln(int(sys.argv[1]) % int(sys.argv[2]))

#phep luy thua
stdio.write(sys.argv[1] + '**' + sys.argv[2] + '=')
stdio.writeln(int(sys.argv[1]) ** int(sys.argv[2]))

#min(a,b)
stdio.write('min (%s, %s) = ' % (sys.argv[1], sys.argv[2]))
stdio.writeln( min (int(sys.argv[1]) , int(sys.argv[2])))

#max(a,b)
stdio.write('max (%s, %s) = ' % (sys.argv[1], sys.argv[2]))
stdio.writeln( max (int(sys.argv[1]) , int(sys.argv[2])))

#abs(a)
stdio.write('abs (%s) = ' % sys.argv[1])
stdio.writeln( abs (int(sys.argv[1])) )

#abs(b)
stdio.write('abs (%s) = ' % sys.argv[2])
stdio.writeln( abs (int(sys.argv[2])) )

