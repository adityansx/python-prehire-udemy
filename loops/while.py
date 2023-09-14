i = 0

while i < 5:
	print(i)
	i += 1

else:
	print('i is greater than 4') 
	# python has else statement that runs when the condition
	# in while is no longer true

for char in 'random':
	pass 
	# pass keyword is used as an empty placeholder
	# if not used, python will keep expecting code after the 'for' line
	# and it'll end up in an error

# break and continue works the same as other langs
# continue moves the execution control to the closest loop statement
# break steps out of the loop block it is enclosed in