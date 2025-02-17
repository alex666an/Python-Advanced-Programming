size = int(input())
matrix = [list(input()) for _ in range(size)]

positions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, 2),
    (1, -2)
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attack_positions = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'K':
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_col < size and 0 <= pos_row < size:
                        if matrix[pos_row][pos_col] == 'K':
                            attacks += 1

                if attacks > max_attacks:
                    knight_with_most_attack_positions = [row, col]
                    max_attacks = attacks

    if knight_with_most_attack_positions:
        r, c = knight_with_most_attack_positions
        matrix[r][c] = 'O'
        removed_knights += 1
    else:
        break

print(removed_knights)