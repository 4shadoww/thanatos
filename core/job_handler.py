# Import python modules

# Import core modules
from core import check_page
from core.algorithm_loader import *
from core import config
from core import adiffer
from core import colors
from core.log import *
from core import wikipedia_worker
import threading, queue
import webbrowser
import pywikibot.exceptions

class PageLoader(threading.Thread):
	running = True
	pages = None
	pageobjects = None
	killer = None

	def __init__(self, pages, pageobjects, killer):
		self.pages = pages
		self.pageobjects = pageobjects
		self.killer = killer
		threading.Thread.__init__(self)

	def run(self):
		for page in self.pages:
			if page.isspace():
				continue
			self.pageobjects.append(wikipedia_worker.loadpage(page))
			if self.killer.kill == True:
				return
		self.running = False

class PageSaver(threading.Thread):
	wpage = None
	comments = None

	def __init__(self, wpage, comments):
		self.wpage = wpage
		self.comments = comments
		threading.Thread.__init__(self)

	def run(self):
		try:
			self.wpage.save(self.comments)
		except pywikibot.exceptions.EditConflict:
			pass

class Killer():
	kill = False

	def __init__(self):
		self.kill = False

def page_handler(algorithms, pageobjects, pageloader):
	pagenum = 0
	while True:
		for i in range(pagenum, len(pageobjects)):
			printlog("checking: "+str(pageobjects[pagenum][1]))
			data = check_page.run(pageobjects[pagenum][2], pageobjects[pagenum][3], algorithms)
			if data[2] == False:
				save_page(pageobjects[pagenum][1], pageobjects[pagenum][2], data[0], data[1])
			pagenum += 1
		if pageloader.running == False and pagenum == len(pageobjects)-1:
			break

def check_pages(pages):
	try:
		killer = Killer()
		killer.__init__()

		algorithms = load_algorithms()
		pageobjects = []
		# Start pageloader thread
		pageloader = PageLoader(pages, pageobjects, killer)
		pageloader.start()

		page_handler(algorithms, pageobjects, pageloader)

		print("saving pages...")
	except KeyboardInterrupt:
		killer.kill = True
		print()
		raise


def save_page(wpage, text, newtext, comments):
	if text == '':
		printlog("error: this page is empty or it doesn't exist")
		return

	if comments == None:
		comments = "thanatos bot edit"

	if newtext != text:
		if config.review == True:
			adiffer.show_diff(text, newtext)
			print(colors.yellow+str(wpage)+": "+comments+colors.end)
			answer = input('do you agree these changes? [Y/N] ')
			if answer == 'p':
				print(newtext)
				answer = input('do you agree these changes? [Y/N] ')
			elif answer == 'e':
				artc = str(wpage).replace("[["+config.lang+":", "").replace("]]", "")
				webbrowser.open_new_tab("https://"+config.lang+".wikipedia.org/w/index.php?title="+artc+"&action=edit")
			if answer == 'y' or answer == 'Y':
				pass
			else:
				return
			wpage.text = newtext
			pagesaver = PageSaver(wpage, comments)
			pagesaver.start()

		else:
			wpage.text = newtext
			pagesaver = PageSaver(wpage, comments)
			pagesaver.start()