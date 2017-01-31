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
		if data[0] == tag:
			return True
	return False


def getword(id, lang=None):
	if lang == None:
		wl = globals()[config.lang]
		return wl[id]
	
	wl = globals()[lang]
	return wl[id]

def getwordlc(id, lang=None):
	if lang == None:
		wl = globals()[config.lang]
		return wl[id].lower()
	
	wl = globals()[lang]
	return wl[id].lower()

def getwordlcc(id, lang=None):
	if lang == None:
		wl = globals()[config.lang]
		return wl[id].lower()+":"
	
	wl = globals()[lang]
	return wl[id].lower()+":"

def getwordulc(id, lang=None):
	if lang == None:
		wl = globals()[config.lang]
		return wl[id], wl[id].lower()
	
	wl = globals()[lang]
	return wl[id], wl[id].lower()

def getwordc(id, lang=None):
	if lang == None:
		wl = globals()[config.lang]
		return wl[id]+":"
	
	wl = globals()[lang]
	return wl[id]+":"

def titlein(title, text):
	titles = re.findall(r"\=.*\=", text)
	for i in titles:
		if re.sub('[^a-zA-Z0-9åäöÅÄÖ]', '', i) == re.sub('[^a-zA-Z0-9åäöÅÄÖ]', '', title):
			return True

	return False

def titlepos(title, text):
	titles = re.findall(r"\=.*\=", text)
	for i in titles:
		if re.sub('[^a-zA-Z0-9åäöÅÄÖ]', '', i) == re.sub('[^a-zA-Z0-9åäöÅÄÖ]', '', title):
			return text.find(i)

	return False

def titleline(title, text):
	for l, line in enumerate(text.split("\n")):
		titles = re.findall(r"\=.*\=", line)
		for item in titles:
			if re.sub('[^a-zA-Z0-9åäöÅÄÖ]', '', item) == re.sub('[^a-zA-Z0-9åäöÅÄÖ]', '', title):
				return l

	return False

def zeromatch(items, text):
	for item in items:
		if item in text:
			print("match "+item+" "+text)
			return False

	return True

def anymatch(items, text):
	for item in items:
		if item in text:
			return True

	return False

def abandop(items, match):
	for item in items:
		if item == match:
			return True
	return False
