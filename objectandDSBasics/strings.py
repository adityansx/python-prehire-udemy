# string slicing
a = 'hello world!'
b = a[0:4]

# len() returns length of the string
print(b + '\tworld', len(b))

# if nothing is mentioned after colon, it slices the string 
# up until the end
print(a[6:])

# same for no number being mentioned before the colon,
# the substring up until that index - 1 is returned
print(a[:5])

# char_array[start from this index: go upto this index but 
# do not include it: step size(optional)]
print(a[2:7])

# step size is the number of chars to jump over
print(a[::2]) # output: 'hlowrd'
# a[::] returns the whole string

# python trick to reverse a string
print(a[::-1])

print('\n--------------------------\n')

# yes, python has string multiplication
# can't get weirder than this, right?
print(a * 2)

# unlike javascript, python doesn't allow implicit 
# type conversion while adding a int to a string.
# It throws an error
print(2 + '2')