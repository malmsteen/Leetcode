def binary_search(list, target):
    high = len(list)-1
    low = 0
    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


my_list = [1, 3, 5, 7, 9, 34, 56, 60, 70, 74, 80, 90]

print(binary_search(my_list, 7))
print(binary_search(my_list, 10))
print(binary_search(my_list, 4))
print(binary_search(my_list, 34))
