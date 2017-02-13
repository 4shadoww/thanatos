def loadpages(file):
	try:
		f = open("core/articles/"+file, 'r')
	except FileNotFoundError:
		print('error: file not found')
		return

	pages = []

	for line in f.read().splitlines():
		if line != "":
			pages.append(line)
	return pages
