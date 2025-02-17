numbers = tuple([float(element) for element in input().split()])
same_values = {}

for num in numbers:
    if num not in same_values:
        same_values[num] = numbers.count(num)

for number, occurrence in same_values.items():
    print(f"{number} - {occurrence} times")