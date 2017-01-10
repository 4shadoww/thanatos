import datetime
import io
from core import config

time = datetime.datetime.now()
logfilename = str(time)
logfile = open('core/log/'+logfilename+'.log', 'a')

def printlog(*log):
		time = datetime.datetime.now()
		line = str(time)+' '+str(log[0])+'\n\n'
		if config.log == True:
			logfile.write(line)
		print(time,str(log[0])+'\n')

def log(*log):
	if config.log == True:
		time = datetime.datetime.now()
		line = str(time)+' '+str(log[0])+'\n\n'
		logfile.write(line)