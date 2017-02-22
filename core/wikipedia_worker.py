# Import pywikibot
import pywikibot
from pywikibot import pagegenerators

from core import config

def loadpage(page):
	try:
		if not config.test:
			site = pywikibot.Site()
			site.throttle.setDelays(delay=0, writedelay=5, absolute=False)
			wpage = pywikibot.Page(site, page)
			text = str(wpage.text)

	except pywikibot.exceptions.InvalidTitle:
		return

	return site, wpage, text, page
