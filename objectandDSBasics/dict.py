# dictionaries are unordered, mutable data structure 
# that store values in a key:value pair
myDict = {
	'name': 'Alice',
	'age': 21,
	3: 89,
	'x': {
		'key1': 'val1'
	},
	'y': [29, 46, 57],
}

print(myDict[3])
print(myDict['x']['key1'])
print(myDict['y'][2], '\n')

print(myDict.keys())
print(myDict.values())
print(myDict.items())