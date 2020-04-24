import subprocess
import sys
import re
import os

def get_pids(port):

	command = "lsof -i :%s | awk '{print $2}'" % port
	pids = subprocess.check_output(command, shell=True)
	pids = pids.strip().decode('utf-8')
	if pids:
		pids = re.sub(' +', ' ', pids)
		for pid in pids.split('\n'):
			try:
				yield int(pid)
			except:
				pass


def close():

    port = 8000
    pids = set(get_pids(port))
    command = 'kill -9 {}'.format(' '.join([str(pid) for pid in pids]))
    os.system(command)
