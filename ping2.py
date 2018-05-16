import subprocess as sb
import time

ping =[]
start = time.time()
for i in range(1,255):
	for n in range(1,256):
		for m in range(1,256):
			for l in range(1,255):
				add = 'ping -n 1 {}.{}.{}.{}'.format(i,n,m,l)
				try:
					result = sb.check_output(add)
				except:
					print('{}へのping失敗'.format(add))
				else:
					print('{}へのping成功'.format(add))
					ping.append(add)
rel = time.time()-start

for x in range(len(ping)):
	print(ping[x])

print("実行時間{}秒".format(rel))
