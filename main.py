n = int(input())

counter = 1
matrix = []
matrix_size = 2 * n + 1
for y in range(matrix_size):
    for x in range(matrix_size):
        if y == x:
            print('0 ', end='')
            continue

        if (y % 2 != 0) ^ (x % 2 == 0):
            zeros = x - 1 if y < x else x
            value = zeros - ((matrix_size * x + y) // 2)
            print(value, end=' ')
        else:
            print(counter, end=' ')
            counter += 1

    print()
