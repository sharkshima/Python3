import subprocess as sb
import time

ping =[]
'''
pingしたいアドレスを入力
１アドレスごとに改行
eを入力することでping開始
'''

while True :
    N = input()
    if N=="e":
    	break
	ping.append(N)

flg = 0
while True:
	try:
		sb.check_output('ping -n 1 {}'.format(ping[flg]))
	except:
	    print('{}へのping失敗'.format(ping[flg]))
	else:
		print('{}へのping成功'.format(ping[flg]))

	if flg==(len(ping)-1):
		flg = 0
	else:
		lg +=1
	
	time.sleep(1)
