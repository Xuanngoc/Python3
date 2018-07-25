import stdio


stdio.write('Mời bạn nhập điểm giữa kì: ')
Dgiuaki = stdio.readFloat()
stdio.write('Mới bạn nhập điểm cuối kỳ: ')
Dcuoiki = stdio.readFloat()
stdio.write('Mới bạn nhập số buổi vắng: ')
Solanvang = stdio.readInt()


Dcc = 10 - Solanvang
Dqt = Dcc * 0.3 + Dgiuaki * 0.7


if Solanvang > 3 or Dqt < 4:
	stdio.writeln('Cấm thi')
else:
	Dtb = Dqt * 0.3 + Dcuoiki * 0.7
	stdio.writeln('Điểm trung bình: %s' % Dtb )
	if Dtb >= 9:
		stdio.writeln('Xuất sắc')
	elif Dtb >= 8:
		stdio.writeln('Giỏi')
	elif Dtb >= 6.5:
		stdio.writeln('Khá')
	elif Dtb >= 4:
		stdio.writeln('Trung bình')
	elif Dtb < 4:
		stdio.writeln('Kém')				
