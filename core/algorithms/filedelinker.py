import re
from core.algcore import *
from core import wikipedia_worker

class Algorithm:
	zeroedit = False
	error_count = 0
	parse = True

	comments = {
		"fi0": u"poisti toimimattoman tiedostolinkin",
		"fi1": u"poisti toimimattomat tiedostolinkit",
	}

	def __init__(self):
		self.error_count = 0

	def run(self, text, article):

		filelinks = []
		for line in text.split("\n"):
			startpos = 0
			last = 0
			findingend = False
			for l in range(0, len(line)):
				if line[l] == "[":
					if findingend != True:
						startpos = l
					last += 1
					findingend = True
				if line[l] == "]" and last > 0:
					last -= 1
				if findingend and last == 0:
					findingend = False
					if getwordc("img") in line[startpos:l+1] or getwordc("file") in line[startpos:l+1]:
						filelinks.append(line[startpos:l+1])

		for file in filelinks:
			if "|" in file and getwordc("img") in file:
				data = wikipedia_worker.loadpage(re.findall(getwordc("img")+r".*?\|", file)[0].replace("|", ""))
			elif "|" in file and getwordc("file") in file:
				data = wikipedia_worker.loadpage(re.findall(getwordc("file")+r".*?\|", file)[0].replace("|", ""))

			else:
				data = wikipedia_worker.loadpage(file.replace("[", "").replace("]", ""))
			if data[2] == "":
				text = text.replace(file, "")
				self.error_count += 1

		return text, self.error_count
