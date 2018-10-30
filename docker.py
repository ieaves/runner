import os
import sys
from subprocess import Popen, PIPE

file = os.path.join(sys.argv[1], 'Jenkinsfile')
#print(sys.argv)
with open(file, 'r') as jf:
	for line in jf.readlines():
		if 'image:' in line:
			ret = line.strip().split('image: ')[1][:-1]
			print(ret)
			break
