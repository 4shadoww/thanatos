from core.algcore import *

class Algorithm:
	notzeroedit = 1
	error_count = 0

	comments = {
		"fi0": u"poisti ylimääräiset hakasulkeet ulkoisesta linkistä",
		"fi1": u"poisti ylimääräiset hakasulkeet ulkoisista linkeistä",
		"en0": u"removed excessive brackets from external link",
		"en1": u"removed excessive brackets from external links"
	}

	def __init__(self):
		self.error_count = 0

	def run(self, text, article):
		nono = [getwordc("file"), getwordc("file", lang="en"), getwordc("img"), getwordc("img", lang="en")]

		twobrackets = re.findall(r"\[(.*?)\]", text)

		for item in twobrackets:
			location = text.index(item)
			if '[' in item[0:2]:
				if 'https://' in item[0:10] or 'http://' in item[0:10]:
					if andop(nono, item) == False:
						self.error_count += 1
						location = text.index(item)+len(item)
						if ']' in text[location+1:location+2]:

							olditem = '['+str(item)+']]'
							item = item.replace('[', '')
							item = '['+item+']'
							log('fix2brackets: '+article+'\n'+olditem+' --> '+item)
							text = text.replace(olditem, str(item))
						else:
							olditem = '['+str(item)+']'
							item = item.replace('[', '')
							item = '['+item+']'
							log('fix2brackets: '+article+'\n'+olditem+' --> '+item)
							text = text.replace(olditem, str(item))

		return text, self.error_count