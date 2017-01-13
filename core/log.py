import datetime
import io
from core import config

time = datetime.datetime.now()
logfilename = str(time)
if config.log == True:
	logfile = open('core/log/'+logfilename+'.log', 'a')

def printlog(*log):
		time = datetime.datetime.now()
		line = str(time)+' '+str(log[0])
		if config.log == True:
			logfile.write(line+"\n")
		print(time,str(log[0]))

def log(*log):
	if config.log == True:
		time = datetime.datetime.now()
		line = str(time)+' '+str(log[0])
		logfile.write(line+"\n")