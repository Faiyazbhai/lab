def find_unique_elements(lst):
    unique = []
    for item in lst:
        if lst.count(item) == 1:
            unique.append(item)
    return unique
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = find_unique_elements(numbers)
print("Unique elements:", unique_numbers)
