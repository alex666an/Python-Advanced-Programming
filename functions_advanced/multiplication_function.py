def multiply(*args):
    result = 1
    for digit in args:
        result *= digit
    return result


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))