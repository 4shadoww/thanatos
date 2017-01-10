def loadpages(file):
	try:
		f = open("core/articles/"+file, 'r')
	except FileNotFoundError:
		print('error: file not found')
		return

	return f.read().splitlines()