

def sum_of_squares(n):
    total = 0
    for digit in str(abs(n)):
        total += int(digit) ** 2
    return total
number = int(input("Enter a number: "))
result = sum_of_squares(number)
print(f"Sum of squares of digits: {result}")
