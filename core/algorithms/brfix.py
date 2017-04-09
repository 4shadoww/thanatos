import re
from core.algcore import *

class Algorithm:
	zeroedit = False
	error_count = 0

	comments = {
		"fi0": u"korjasi br tagin syntaksin tai korvasi sen {{clear}} mallineella",
		"fi1": u"korjasi br tagien syntaksit tai korvasi ne {{clear}} mallineella",
	}

	def __init__(self):
		self.error_count = 0

	def run(self, text, article):
		pattern = r"\<.*?\>"
		parsedtext = wtparser.parse(text)
		text = list(text)
		print(''.join(text))
		errorlist = refindall(pattern, parsedtext)
		print(errorlist)
		text = replacepos("fixed", text, errorlist[3][0], errorlist[3][1])
		print(''.join(text))
		return
		nono = ['abbr', 'wbr', 'ref', '<!--']

		for item in errorlist:
			if andop(nono, item) == False and istag("br", item):
				if 'clear' in item and '=' in item:
					if 'all' in item:
						text = text.replace(item, '{{clear}}')
						self.error_count += 1
					elif 'left' in item:
						text = text.replace(item, '{{clear|left}}')
						self.error_count += 1
					elif 'right' in item:
						text = text.replace(item, '{{clear|right}}')
						self.error_count += 1
				elif '/' in item and item != '<br />' and 'clear' not in item and '=' not in item:
					text = text.replace(item, '<br />')
					self.error_count += 1
				elif '/' not in item and item != '<br>' and 'clear' not in item and '=' not in item:
					text = text.replace(item, '<br>')
					self.error_count += 1

		return text, self.error_count
