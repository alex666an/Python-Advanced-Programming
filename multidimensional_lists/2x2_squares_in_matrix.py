rows, cows = [int(el) for el in input().split()]
matrix = [input().split() for _ in range(rows)]

equals = 0

for row in range(rows - 1):
    for cow in range(cows - 1):
        symbol = matrix[row][cow]

        if symbol == matrix[row + 1][cow] and symbol == matrix[row][cow + 1] and symbol == matrix[row + 1][cow + 1]:
            equals += 1

print(equals)
