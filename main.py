def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal

binary_input = input("Enter your Binary: ")
decimal_output = binary_to_decimal(binary_input)
print(f"Decimal: {decimal_output}")
