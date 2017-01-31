import datetime
import io
from core import config

time = datetime.datetime.now()
logfilename = str(time)
if config.enable_log == True:
	logfile = open('core/log/'+logfilename+'.log', 'a')

def printlog(*message):
		time = datetime.datetime.now()
		line = str(time)+' '+str(message[0])
		if config.enable_log == True:
			logfile.write(line+"\n")
		print(time,str(message[0]))

def log(*message):
	if config.enable_log == True:
		time = datetime.datetime.now()
		line = str(time)+' '+str(message[0])
		logfile.write(line+"\n")