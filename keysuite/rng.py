import random

def varsh(var):
	var_list = list(var)
	random.shuffle(var_list)
	return ''.join(var_list)

