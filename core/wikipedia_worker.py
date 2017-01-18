# Import pywikibot
import pywikibot
from pywikibot import pagegenerators

def loadpage(page):
	try:
		site = pywikibot.Site()
		wpage = pywikibot.Page(site, page)
		text = str(wpage.text)

	except pywikibot.exceptions.InvalidTitle:
		return

	return site, wpage, text
