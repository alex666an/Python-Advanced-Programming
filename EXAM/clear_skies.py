def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


def is_valid_position(row, col, size):
    return 0 <= row < size and 0 <= col < size


def find_jetfighter(matrix, size):
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 'J':
                return i, j


def main():
    size = int(input())
    matrix = [list(input()) for _ in range(size)]

    initial_armor = 300
    armor = initial_armor
    jetfighter_r, jetfighter_c = find_jetfighter(matrix, size)
    enemy_count = matrix_count = sum(row.count('E') for row in matrix)

    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }

    while True:
        command = input()
        matrix[jetfighter_r][jetfighter_c] = '-'
        move_row, move_col = directions[command]
        jetfighter_r += move_row
        jetfighter_c += move_col

        if not is_valid_position(jetfighter_r, jetfighter_c, size):
            print("Mission failed, your jetfighter was shot down! Last coordinates [{}, {}]!".format(
                jetfighter_r - move_row, jetfighter_c - move_col))
            break

        if matrix[jetfighter_r][jetfighter_c] == 'E':
            armor -= 100
            enemy_count -= 1
            matrix[jetfighter_r][jetfighter_c] = '-'

            if enemy_count == 0:
                print("Mission accomplished, you neutralized the aerial threat!")
                break

            if armor <= 0:
                print("Mission failed, your jetfighter was shot down! Last coordinates [{}, {}]!".format(
                    jetfighter_r, jetfighter_c))
                break

        elif matrix[jetfighter_r][jetfighter_c] == 'R':
            armor = initial_armor
            matrix[jetfighter_r][jetfighter_c] = '-'

    matrix[jetfighter_r][jetfighter_c] = 'J'  # Place 'J' at the last known position
    print_matrix(matrix)


if __name__ == "__main__":
    main()

