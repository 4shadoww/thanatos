# Import python modules
import importlib
from glob import glob

# Import core modules
from core.config import *

def load_algorithms():
	algorithms = glob("core/algorithms/*.py")
	objects = []

	for algorithm in algorithms:
		algorithm = algorithm.replace(".py", "").replace("core/algorithms/", "")
		if algorithm not in ignore:
			module = importlib.import_module("core.algorithms."+algorithm)
			objects.append(module.Algorithm())

	return objects