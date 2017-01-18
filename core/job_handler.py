# Import python modules

# Import core modules
from core import check_page
from core.algorithm_loader import *
from core import config
from core import adiffer
from core import colors
from core.log import *
from core import wikipedia_worker

def check_pages(pages):
	algorithms = load_algorithms()

	for page in pages:
		if page.isspace():
			continue

		wikidata = wikipedia_worker.loadpage(page)
		printlog("checking: "+str(wikidata[1]))
		data = check_page.run(wikidata[2], page, algorithms)

		save_page(wikidata[1], wikidata[2], data[0], data[1])


def save_page(wpage, text, newtext, comments):
	if text == '':
		printlog("error: this page is empty or it doesn't exist")
		return

	if comments == None:
		comments = "Bot edit"

	if newtext != text:
		if config.review == True:
			adiffer.show_diff(text, newtext)
			print(colors.yellow+str(wpage)+": "+comments+colors.end)
			answer = input('do you agree these changes? [Y/N] ')
			if answer == 'p':
				print(newtext)
				answer = input('do you agree these changes? [Y/N] ')
			if answer == 'y' or answer == 'Y':
				pass
			else:
				return
			wpage.text = newtext
			wpage.save(comments)

		else:
			wpage.text = newtext
			wpage.save(comments)