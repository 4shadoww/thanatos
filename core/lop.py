import re
from core import config
from core.langdict import *
from core.log import *

warnings = {
	"war0fi": "lop ristiriita: kaksi samanlaista riviä",
}

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
	startpos = titleline(title, text)
	text = text.split("\n")
	endpos = len(text)
	belows = text[startpos:endpos]
	tries = 0
	lasttemp = 0
	listfound = False
	for l in  range(0, len(belows)):
		if l == 0:
			continue

		if abandop(spaces, belows[l]):
			tries += 1

		else:
			tries = 0

		if l == 3 and listfound == False:
			endpos = len(text)-len(belows)
			break

		if tries >= 2:
			endpos = len(text)-len(belows)+l
			break

		if istitle(belows[l]) and "===" not in belows[l]:
			endpos = len(text)-len(belows)+l-1
			break

		if anymatch(listitems, belows[l]):
			listfound = True

		if listfound and lasttemp > 0:
			continue

		if anymatch(listitems, belows[l]) and "{{" in belows[l]:
			lasttemp += belows[l].count("{{")

		if "}}" in belows[l] and lasttemp > 0:
			lasttemp -= belows[l].count("}}")
			continue

		if anymatch(nono, belows[l]):
			endpos = len(text)-len(belows)+l-1
			break

		if zeromatch(listitems, belows[l]) and listfound and zeromatch(listitems, belows[l+1]):
			endpos = len(text)-len(belows)+l
			break

	return startpos, endpos, listfound

def removefromlist(sec, listobj):
	startpos = 0
	foundstart = False
	endpos = len(listobj)
	foundend = False

	for l in range(0, len(listobj)):
		if sec[0] == listobj[l]:
			startpos = l
			if foundstart == True:
				warning(warnings["war0"+config.lang])

			foundstart = True
		if sec[len(sec)-1] == listobj[l]:
			endpos = l

			if foundend == True:
				warning(warnings["war0"+config.lang])

			foundend = True
	print(startpos, endpos)
	for l,t in zip(range(startpos, endpos+1), range(0, endpos-startpos+1)):
		listobj.pop(l-t)
	return listobj