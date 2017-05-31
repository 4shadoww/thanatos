from core.algcore import *

class Algorithm:
	zeroedit = False
	error_count = 0
	parse = True

	comments = {
		"fi0": u"korjasi linkin",
		"fi1": u"korjasi linkkejä",
		"en0": u"fixed link",
		"en1": u"fixed links"
	}

	def __init__(self):
		self.error_count = 0

	def run(self, page, text):
		linkpartlist = []
		fixedlinks = []
		invalidlinks = []
		characters = 'abcdefghijklmnopqrstuvxyzäöABCDEFGHIJKLMNOPQRSTUVXYZŽÄÖ!?*[]{}()0123456789'
		special = '!?*[]{}()'
		twobrackets = re.findall(r"\[(\S+)\]", text)
		for hit in twobrackets:
			link = str(hit)
			matches = re.search(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}', link)
			if 'http://' not in link and 'https://' not in link and matches != None and 'ref' not in link and '@' not in link and '[' not in link and '{' not in link[0:2]:
				orglink = '['+link+']'
				self.error_count += 1
				linkpartlist = link.split('.')

				if len(linkpartlist) >= 3 and 'w' in linkpartlist[0] and linkpartlist[0] != 'www':
					if any((char in linkpartlist[0]) for char in characters):
						if any((char in linkpartlist[0]) for char in special):
							continue
					else:
						if len(linkpartlist[0]) != 3:
							linkpartlist[0] = 'www'
							time = 0
							finallink = ''
							for item in linkpartlist:
								time += 1
								if time != len(linkpartlist):
									finallink = finallink+item+'.'
								else:
									finallink = finallink+item
							link = '[http://'+finallink+']'
							log('fixblink invalid link found: '+article+'\n'+orglink+' --> '+link)
							text = text.replace(orglink, link)
							fixedlinks.append(link)
							invalidlinks.append(orglink)
						else:
							printlog('www fix error')

				else:
					link = '[http://'+link+']'
					log('fixblink invalid link found: '+article+'\n'+orglink+' --> '+link)
					fixedlinks.append(link)
					invalidlinks.append(orglink)
					text = text.replace(orglink, link)

		return text, self.error_count
