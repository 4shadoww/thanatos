# Import python modules


# Import core modules
from core import config

def run(text, page, algorithms):
	edit_comments = []
	for algorithm in algorithms:
		algorithm.__init__()
		data = algorithm.run(text, page)
		if data[1] == 1:
			edit_comments.append(algorithm.comments[config.lang]+"0")
		elif data[1] > 1:
			edit_comments.append(algorithm.comments[config.lang]+"1")