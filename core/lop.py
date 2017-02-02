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
		data = re.sub('[^a-zA-Z0-9 ]', ' ', data).split()

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

def istitle(title):
	titles = re.findall(r"\=.*\=", title)

	if len(titles) > 0 and re.sub('[^a-zA-Z0-9åäöÅÄÖ]', '', titles[0]) == re.sub('[^a-zA-Z0-9åäöÅÄÖ]', '', title):
		return True

	return False

def titlebefore(after, before, text):
	text = text.split("\n")
	nextref = False

	for line in text:
		if titlein(after, line):
			nextref = True
			continue
		if titlein(before, line) and nextref:
			return True
		elif istitle(line) and nextref:
			return False
	return False

def listend(text, title, listitems, nono, spaces):
	startpos = titleline(getwordc("srcs"), text)
	text = text.split("\n")
	endpos = len(text)
	belows = text[startpos:len(text)]
	tries = 0
	lasttemp = False
	listfound = False
	for l, line in  enumerate(belows[1:]):
		if abandop(spaces, line):
			tries += 1

		else:
			tries = 0

		if l == 2 and listfound == False:
			endpos = len(text)-len(belows)
			break

		if tries >= 2:
			endpos = len(text)-len(belows)+l
			break

		if anymatch(listitems, line):
			listfound = True

		if listfound and "|" in line and lasttemp:
			continue

		if anymatch(listitems, line) and "{{" in line:
			lasttemp = True

		if "}}" in line and lasttemp:
			lasttemp = False
			continue
			
		if anymatch(nono, line):
			endpos = len(text)-len(belows)+l
			break

		elif zeromatch(listitems, line) and line != "" and listfound and zeromatch(listitems, belows[l+1]):
			endpos = len(text)-len(belows)+l+1
			break

	return startpos, endpos, listfound