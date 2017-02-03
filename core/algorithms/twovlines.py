from core.algcore import *
import re

class Algorithm:
	zeroedit = False
	error_count = 0

	comments = {
		"fi0": u"poisti ylimääräisen pystyviivan",
		"fi1": u"poisti ylimääräiset pystyviivat",

	}

	def __init__(self):
		self.error_count = 0

	def run(self, text, article):
		brackets = re.findall(r"\[(.*?)\]", text)
		for item in brackets:
			if '||' in item and getword("img") not in item and getword("file")  not in item and 'Image:' not in item and 'File:' not in item:
				self.error_count += 1
				olditem = '['+item+']]'
				item = '['+item+']]'
				item = item.replace('||', '|')
				log('twovlines invalid link found: '+article+'\n'+olditem+' --> '+item)
				text = text.replace(olditem, item)
		return text, self.error_count