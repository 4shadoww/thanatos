from core.algcore import *

class Algorithm:
	zeroedit = True
	error_count = 0
	parse = True

	comments = {
		"fi0": u"poisti wikipedian sisäisestä linkistä tekstin jossa se on sama kuin linkki",
		"fi1": u"poisti wikipedian sisäisistä linkeistä tekstin joissa se on sama kuin linkki",
		"en0": u"removed text from pipedlink because it was same as link",
		"en1": u"removed texts from pipedlinks because it was same as link"
	}

	def __init__(self):
		self.error_count = 0

	def run(self, page):
		text = page.text

		searchtext = text.replace(' ', '_')
		twobrackets = re.findall(r"\[(\S+?)\]", searchtext )

		for item in twobrackets:
			fixeditem = None
			originalitem = item
			if '|' in item:
				item = item.replace('[', '').replace(']', '')
				item = item.split('|')

				if item[0] == item[1]:
					fixeditem = '['+str(item[0])+''
					fixeditem = fixeditem.replace('_', ' ')
				if fixeditem != None:
					self.error_count += 1
					originalitem = originalitem.replace('_', ' ')
					log('fixpiped invalid links found: '+page.title()+'\n'+originalitem+'] --> '+fixeditem+']')
					text = text.replace(str(originalitem), str(fixeditem))

		return text, self.error_count
