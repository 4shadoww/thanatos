from core.algcore import *
from pywikibot.site import APISite
import pywikibot

class Algorithm:
	zeroedit = False
	error_count = 0
	parse = True

	comments = {
		"fi0": "korjasi ulkoisen linkin",
		"fi1": "korjasi ulkoisia linkkejä",
	}

	api = APISite(core.config.lang)

	def __init__(self):
		self.error_count = 0

	def run(self, page, text):
		target = "http://www.eurohockey.net/players/show_player.cgi?serial="
		newlink = "http://www.eurohockey.com/player/"

		for link in self.api.page_extlinks(page):
			if link.startswith(target):
				idl = link.split(target)[1]
				if isInt(idl):
					newid = str(int(idl)+123)
					text = text.replace(link, newlink+newid+"-.html")
					self.error_count += 1
		return text, self.error_count
