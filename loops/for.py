# basic for loop
myList = [1, 2, 4, 8, 16]

for num in myList:
	print(num)

# unpacking tuples
myList = [(1, 2), (3, 4), (5, 6)]

for x, y in myList:
	print(x, y)

# iterating over dict
myDict = {
	'name': 'Alice',
	'age': 27,
	'country': 'Australia'
}

# python iterates over keys by default

for item in myDict:
	print(f'{item}: {myDict[item]}')

# the following code can be refactored as

for (key, value) in myDict.items():
	print(f'{key}: {value}')