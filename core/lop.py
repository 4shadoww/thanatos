import re
from core import config
from core.langdict import *

def andop(items, text):
	for item in items:
		if item in text:
			return True
	return False

def istag(tag, data):
	if data.count("<") == 1 and data.count(">") == 1 and tag in data:
		data = re.sub('[^a-zA-Z0-9 ]', ' ', data)
		for word in data.split():
			if word == tag:
				return True
	return False


def getword(id, lang=None):
	if lang == None:
		wl = globals()[config.lang]
		return wl[id]
	
	wl = globals()[lang]
	return wl[id]

def getwordc(id, lang=None):
	if lang == None:
		wl = globals()[config.lang]
		return wl[id]+":"
	
	wl = globals()[lang]
	return wl[id]+":"