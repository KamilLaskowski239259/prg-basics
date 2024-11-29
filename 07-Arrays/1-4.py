###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('last value', arr[len(arr) - 1])
print('last but one value', arr[len(arr) - 2])
print('first + last value', arr[0]+arr[-1])
print('middle value', arr[len(arr)//2])
for i in arr:
    print(i)
