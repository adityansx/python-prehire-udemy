def has_even_num(numbers):
	for num in numbers:
		if num % 2 == 0:
			return True
		
print(has_even_num([1, 3, 5, 7, 8]))