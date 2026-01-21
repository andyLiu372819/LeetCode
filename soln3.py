import math


def spiral(matrix):
    def move(i, j, dir):
        if dir == 'l':
            return i, j - 1
        if dir == 'r':
            return i, j + 1
        if dir == 'u':
            return i - 1, j
        if dir == 'd':
            return i + 1, j

    def change_dir(dir_index):
        if dir_index == 3:
            return 0
        return dir_index + 1

    direction = ['r', 'd', 'l', 'u']
    dir_index = 0
    m, n = len(matrix), len(matrix[0])
    total = m * n
    count = 0
    i, j = 0, 0
    change_i, change_j = False, True
    res = []
    while count < total:
        res.append(matrix[i][j])
        if (i == m - 1 and change_i) or (j == n - 1 and change_j):
            dir_index = change_dir(dir_index)
            change_i, change_j = not change_i, not change_j
        i, j = move(i, j, direction[dir_index])
        count += 1
    return res


print(spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

