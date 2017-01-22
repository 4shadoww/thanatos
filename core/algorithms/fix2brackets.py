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

		textlist = text.split('\n')
		for l, line in enumerate(textlist):
			matches = re.findall(r"\[.*\]", line)
			for match in matches:
				if 'https://' in match or 'http://' in match:
					if match.count("[") >= 2 or match.count("]") >= 2:
						newmatch = "["+match.replace("[", "").replace("]", "")+"]"
						textlist[l] = textlist[l].replace(match, newmatch)
						self.error_count += 1

		text = '\n'.join(textlist)
		return text, self.error_count