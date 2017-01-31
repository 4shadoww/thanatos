# Import python modules
import importlib
from core import config

# Import core modules
from core.config import *

def load_algorithms():
	objects = []

	for algorithm in algorithms:
		if algorithm not in ignore:
			module = importlib.import_module("core.algorithms."+algorithm)
			objects.append(module.Algorithm())

	return objects