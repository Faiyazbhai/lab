
def binary_search(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
target = int(input("Enter the number to search: "))

result = binary_search(sorted_list, target, 0, len(sorted_list) - 1)

if result != -1:
    print(f"Number found at index {result}")
else:
    print("Number not found in the list")
