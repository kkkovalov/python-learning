from array import *

arr = array('i', [1,5,8,12,53,2,76,45])

print(arr[4])
print(len(arr))
#Functions such as: append(), extend(), insert(i,x)
# append() - one more value at the back
# extend() - many values at the back
# insert() - add a value in specified (i position)

arr.append(4)
arr.extend([34,2])
arr.insert(2341, 3)

nArr = array('i', [534, 34, 40, 20])

arr = arr + nArr

# Remove items from array: pop(), remove()
# pop() - removes last element and returns the value
# remove() - removes last element and does NOT return it

print("Removed:",arr.pop())
print("Removed:",arr.remove())

print("Array: ")
for i in arr:
    print("Value: ", i)

