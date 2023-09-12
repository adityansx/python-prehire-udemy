myFile = open('./test.txt')

print(myFile.read())


with open('./test.txt', mode='a') as myOtherFile:
	myOtherFile.write('\nthird line')

print(myFile.read())

with open('randomName.txt', mode='w+') as newFile:
	newFile.write('This is a newly created file\n')

with open('randomName.txt', mode='r') as newFile:
	print(newFile.read())

myFile.close()