from core.algcore import *

class Algorithm:
	zeroedit = False
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
		parser = wtparser.Parser()
		text = parser.parse(text)
		nono = [getwordc("file"), getwordc("file", lang="en"), getwordc("img"), getwordc("img", lang="en")]

		textlist = text.split('\n')
		for l, line in enumerate(textlist):
			matches = re.findall(r"\[.*?\]", line)
			for match in matches:
				if 'https://' in match and match.count("[") < 2 and "|" not in match or 'http://' in match and match.count("[") < 2 and "|" not in match:
					if match.count("[") >= 2 or match.count("]") >= 2:
						newmatch = "["+match.replace("[", "").replace("]", "")+"]"
						textlist[l] = textlist[l].replace(match, newmatch)
						self.error_count += 1

		text = '\n'.join(textlist)
		text = parser.deparse(text)
		return text, self.error_count
