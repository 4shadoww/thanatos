# Import python modules

# Import pywikibot
import pywikibot
from pywikibot import pagegenerators

# Import core modules
from core import check_page
from core.algorithm_loader import *
from core import config
from core import adiffer
from core import colors

def check_pages(pages):
	algorithms = load_algorithms()

	for page in pages:
		if page.isspace():
			continue

		try:
			site = pywikibot.Site()
			wpage = pywikibot.Page(site, page)
			text = str(wpage.text)
			newtext = check_page.run(text, page, algorithms)

		except pywikibot.exceptions.InvalidTitle:
				continue

		save_page(text, newtext)


def save_page(text, newtext):
	if text == '':
			printlog("error: this page is empty or it doesn't exist")
			continue

		if newtext != text:
			if config.review == True:
				adiffer.show_diff(text, newtext)
				print(colors.yellow+page+": "+saves+colors.end)
				answer = input('do you agree these changes? [Y/N] ')
				if answer == 'p':
					print(newtext)
					answer = input('do you agree these changes? [Y/N] ')
				if answer == 'y' or answer == 'Y':
					pass
				else:
					continue
				wpage.text = newtext
				wpage.save("edit comment")

			else:
				wpage.text = newtext
				wpage.save("edit comment")