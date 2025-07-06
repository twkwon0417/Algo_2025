ls = []
zero = []


def is_good(idx):
    y, x = zero[idx]
    num = ls[y][x]

    for j in range(9):
        if j != x and ls[y][j] == num:
            return False

    for i in range(9):
        if i != y and ls[i][x] == num:
            return False

    start_y = (y // 3) * 3
    start_x = (x // 3) * 3
    for i in range(start_y, start_y + 3):
        for j in range(start_x, start_x + 3):
            if (i, j) != (y, x) and ls[i][j] == num:
                return False

    return True


for i in range(9):
    line = input()
    row = [int(char) for char in line]
    ls.append(row)

for i in range(9):
    for j in range(9):
        if ls[i][j] == 0:
            zero.append((i, j))

idx = 0
while idx < len(zero):
    y, x = zero[idx]

    if ls[y][x] == 9:
        ls[y][x] = 0
        idx -= 1
        continue

    ls[y][x] += 1

    if is_good(idx):
        idx += 1
    else:
        continue

for row in ls:
    print("".join(map(str, row)))