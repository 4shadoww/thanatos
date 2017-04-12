import re
from core.algcore import *
import html

class Algorithm:
	zeroedit = False
	error_count = 0

	comments = {
		"fi0": u"korjasi linkin",
		"fi1": u"korjasi linkkejä",

		"en0": "fixed link",
		"en1": "fixed links"
	}

	def __init__(self):
		self.error_count = 0

	def run(self, text, article):
		parser = wtparser.Parser()
		text = parser.parse(text)
		linkpartlist = []
		fixedlinks = []
		invalidlinks = []

		characters = 'abcdefghijklmnopqrstuvxyzäöABCDEFGHIJKLMNOPQRSTUVXYZŽÄÖ!?*[]{}()0123456789'
		special = '!?*[]{}()'
		refs = re.findall(r"\<ref>.*?\</ref>", text)

		for hit in refs:
			link = str(hit)
			orglink = link
			link = link.replace('<ref>', '').replace('</ref>', '')
			matches = re.search(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}', link)
			if 'http://' not in link and 'https://' not in link and matches != None and 'ref' not in link and '@' not in link and '{' not in link[0:2] and '[' not in link[1:2] and 'ftp://' not in link and "'" not in link[0:2]:
				if '[' in link and ']' in  link:
					linkpartlist = link.split('.')
					if ' ' in linkpartlist[0][1:] or ' ' in linkpartlist[1][0:1]:
						continue
					if len(linkpartlist) >= 3 and 'w' in linkpartlist[0] and linkpartlist[0] != 'www':
						if '[' not in linkpartlist[0][0:1] and any((char in linkpartlist[0]) for char in characters):
							if any((char in linkpartlist[0]) for char in special):
								log('fixreflinks: special mark found getting out')
								continue
						else:
							if len(linkpartlist[0]) != 3 or '[' in linkpartlist[0]:
								linkpartlist[0] = 'www'
								time = 0
								finallink = ''
								for item in linkpartlist:
									time += 1
									if time != len(linkpartlist):
										finallink = finallink+item+'.'
									else:
										finallink = finallink+item
								link = '<ref>[http://'+finallink+'</ref>'
								log('fixreflink invalid link found: '+article+'\n'+orglink+' --> '+link)
								fixedlinks.append(link)
								invalidlinks.append(orglink)
							else:
								printlog('www fix error: '+ str(linkpartlist))

					else:
						link = link.replace('[','')
						link = '<ref>[http://'+link+'</ref>'
						log('fixreflink invalid link found: '+article+'\n'+orglink+' --> '+link)
						fixedlinks.append(link)
						invalidlinks.append(orglink)
				else:
					linkpartlist = link.split('.')
					if ' ' in linkpartlist[0][1:] or ' ' in linkpartlist[1][0:1]:
						continue
					if len(linkpartlist) >= 3 and 'w' in linkpartlist[0] and linkpartlist[0] != 'www':
						if any((char in linkpartlist[0]) for char in characters):
							if any((char in linkpartlist[0]) for char in special):
								continue
						else:
							print(linkpartlist[0])
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
								link = '<ref>http://'+finallink+'</ref>'
								log('fixreflink invalid link found: '+article+'\n'+orglink+' --> '+link)
								fixedlinks.append(link)
								invalidlinks.append(orglink)

							else:
								printlog('www fix error: '+ str(linkpartlist))

					else:
						link = '<ref>http://'+link+'</ref>'
						log('fixreflink invalid link found: '+article+'\n'+orglink+' --> '+link)
						fixedlinks.append(link)
						invalidlinks.append(orglink)

		for fixedlink, invalidlink in zip(fixedlinks, invalidlinks):
			self.error_count += 1
			i =  html.unescape(str(invalidlink))
			f = html.unescape(str(fixedlink))
			text = text.replace(i, f)
		text = parser.deparse(text)
		return text, self.error_count
