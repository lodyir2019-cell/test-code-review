def calculate_average(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total / len(numbers)

result = calculate_average([10, 20, 30])
print(result)
