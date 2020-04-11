def listToDictionary(lst):
	return {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}

list = ["Hello","world","simple","test"]
print(listToDictionary(list))

# - OUTPUT - #
#» {'Hello': 'world', 'simple': 'test'}
