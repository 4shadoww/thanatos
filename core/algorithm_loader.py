# Import python modules
import importlib
import core.config

def load_algorithms(algorithms=core.config.algorithms, ignore=core.config.ignore):
	objects = []

	for algorithm in algorithms:
		if algorithm not in ignore:
			module = importlib.import_module("core.algorithms."+algorithm)
			objects.append(module.Algorithm())

	return objects
