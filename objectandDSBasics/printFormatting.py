# string formatting
print('The quick {} {}'.format('fox', 'brown'))

# can print based on the index of args passed into format()
print('The quick {1} {0}'.format('fox', 'brown'))

# or based on named variable
print('The quick {b} {f}'.format(f = 'fox', b = 'brown'))

print('\n----------------------\n')

# float formatting
# {value:width.precisionf}

# P.S.: Don't have whitespaces for decorative purposes,
# python interpreter hates it

result = 100 / 3

print('The result is {res:.2f}'.format(res = result))

# f-string, alike template literals in js
# print(f'The result is {result:.2f}')
print(f'The result is {100 / 3:.2f}')
