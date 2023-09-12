myList = ['one', 'two', 'three']

# unlike strings, items in a list are mutable
myList[0] = myList[0].upper()

# list concatenation
newList = myList + ['four', 'five']

# adding items
newList.append('six')

# removing items
item = newList.pop()
# pop(__index = -1) -> str
# removes the last item in the list by default
# can take an index to delete an item at a particular index
# returns the item deleted from the list

# sorting a list
numList = [2, 3, 1, 6, 3, 5, 7, 28, 19]
numList.sort()

# reversing a list
numList.reverse()
# or
x = numList[::-1]

print(x)