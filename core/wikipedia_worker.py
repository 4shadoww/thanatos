# Import pywikibot
import pywikibot
from pywikibot import pagegenerators
from pywikibot import throttle

def loadpage(page):
	try:
		site = pywikibot.Site()
		thor = throttle.Throttle(site, mindelay=0, maxdelay=0, writedelay=0, multiplydelay=False)
		thor.setDelays(delay=0, writedelay=0, absolute=True)
		wpage = pywikibot.Page(site, page)
		text = str(wpage.text)

	except pywikibot.exceptions.InvalidTitle:
		return

	return site, wpage, text, page
