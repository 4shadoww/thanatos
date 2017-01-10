# Import python modules
from glob import glob

# Import pywikibot
import pywikibot
from pywikibot import pagegenerators

# Import core modules
from core import review
from core import config

algorithms = glob("core/algorithms/*.py")
#print(algorithms)

i = 0
for algorithm in algorithms:
	algorithms[i] = algorithm.replace(".py", "").replace("core/algorithms/", "")
	print(algorithm)
	

def run(page):
	pass
	#print(algorithms)

