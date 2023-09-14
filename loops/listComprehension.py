# converting a string into a list
word = 'letter'

lst = []

for char in word:
	lst.append(char)

# getting unique chracters in a word 
lst = [char for char in set(word)]

# getting a list of even numbers upto 10
lst = [num for num in range(0, 11) if num % 2 == 0]

# square of every even number upto 10
lst = [num ** 2 for num in range(0, 11) if num % 2 == 0]

# nested list comprehension
# every even number upto 10 raised to 4
lst = [num ** 2 for num in [num ** 2 for num in range(0, 11) if num % 2 == 0]]

print(lst)

