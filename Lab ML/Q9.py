def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary
number = int(input("Enter a decimal number: "))
binary_result = decimal_to_binary(number)
print(f"Binary representation: {binary_result}")
