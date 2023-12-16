def print_rocks(r,c, max_i, max_j):
    for i in range(max_i):
        for j in range(max_j):
            if (i,j) in r:
                print('O', end='')
            elif (i,j) in c:
                print('#', end='')
            else:
                print('.', end='')
        print()
        

round_rocks, cube_rocks = set(), set()
field_length = 0
with open('14/input_t.txt', 'r') as f:
    for i, line in enumerate(f.read().strip().split('\n')):
        for j, d in enumerate(line):
            if d == 'O':
                round_rocks.add((i, j))
            elif d == '#':
                cube_rocks.add((i, j))
        field_length += 1
    field_width = len(line)


square_by_col = [
    set([x[0] for x in cube_rocks if x[1] == y])
    for y in range(field_width)
    ]
square_by_row = [
    set([x[1] for x in cube_rocks if x[0] == y])
    for y in range(field_length)
    ]

# north
for j in range(field_width):
    max_i = -1
    for i in range(field_length):
        if i in square_by_col[j]:
            max_i = i
        elif (i,j) in round_rocks:
            round_rocks.remove((i,j))
            max_i += 1
            round_rocks.add((max_i,j))

total_load = 0
for pos in round_rocks:
    total_load += field_length - pos[0]

print_rocks(round_rocks, cube_rocks, field_length, field_width)
print()

print(f'a: The total load caused by all round rocks is {total_load}.')
