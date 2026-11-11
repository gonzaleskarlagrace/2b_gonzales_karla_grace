#1
def sum_array(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_array(arr[1:])

print("Sum:", sum_array([]))
print("Sum:", sum_array([6, 7, 8, 9, 10]))
print("Sum:", sum_array([10]))
print("Sum:", sum_array([-3, 4, -5]))

print()
#2
def largest_number(arr):
    if len(arr) == 0:
        raise ValueError("Array must not be empty")

    if len(arr) == 1:
        return arr[0]

    largest = largest_number(arr[1:])

    if arr[0] > largest:
        return arr[0]
    else:
        return largest


print("Largest:", largest_number([21, 16, 9, 20]))
print("Largest:", largest_number([20]))
print("Largest:", largest_number([4, 5, 14, 19]))
print("Largest:", largest_number([-6, -8, -10]))

print()
#3
def count_number(arr, target):
    if len(arr) == 0:
        return 0

    if arr[0] == target:
        return 1 + count_number(arr[1:], target)
    else:
        return count_number(arr[1:], target)


print("Count:", count_number([2, 2, 4, 3, 2, 5, 2], 2))
print("Count:", count_number([], 5))
print("Count:", count_number([1, 2, 3], 9))