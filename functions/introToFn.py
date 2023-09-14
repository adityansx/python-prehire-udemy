def add_numbers(nums = None):
	'''
		Testing out docstring
	'''
	if(not nums):
		return
	
	sum = 0

	if(not is_iterable(nums)):
		sum = num

	# TODO: Have a better solution for accepting var args

	for num in nums:
		sum += num

	return sum

def is_iterable(obj):
	'''
		Returns True if object is iterable, False if otherwise
	'''

	try:
		iter(obj)
		return True
	except TypeError:
		return False


print(add_numbers((1, 2, 3, 4, 5)))

res = add_numbers([1, 5])

print('' if not res else res)