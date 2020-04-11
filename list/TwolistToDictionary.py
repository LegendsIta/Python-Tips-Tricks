def TwolistToDictionary(lst1,lst2):
	return dict(zip(lst1,lst2))

list1 = ["Hello", "simple"]
list2 = ["world", "test"]
print(TwolistToDictionary(list1,list2))

# - OUTPUT - #
#» {'Hello': 'world', 'simple': 'test'}
