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


def cycle_rocks(round_rocks_frozen):
    global field_width
    global field_length
    global square_by_col
    global square_by_row
    global cube_rocks
    
    round_rocks = set(round_rocks_frozen)
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
    # west
    for i in range(field_length):
        max_j = -1
        for j in range(field_width):
            if j in square_by_row[i]:
                max_j = j
            elif (i,j) in round_rocks:
                round_rocks.remove((i,j))
                max_j += 1
                round_rocks.add((i,max_j))
    # south
    for j in range(field_width-1,-1,-1):
        min_i = field_length
        for i in range(field_length-1,-1,-1):
            if i in square_by_col[j]:
                min_i = i
            elif (i,j) in round_rocks:
                round_rocks.remove((i,j))
                min_i -= 1
                round_rocks.add((min_i,j))
    # east
    for i in range(field_length-1,-1,-1):
        min_j = field_width
        for j in range(field_width,-1,-1):
            if j in square_by_row[i]:
                min_j = j
            elif (i,j) in round_rocks:
                round_rocks.remove((i,j))
                min_j -= 1
                round_rocks.add((i,min_j))
    return frozenset(round_rocks)
                

round_rocks, cube_rocks = set(), set()
field_length = 0
with open('14/input.txt', 'r') as f:
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

memo = {}
round_rocks = frozenset(round_rocks)
for n in range(1000000000):
    if not round_rocks in memo:
        memo[round_rocks] = n
        round_rocks = cycle_rocks(round_rocks)
    else:
        break
print(f'First repeat at cycle {n}, showing same configuration as cycle {memo[round_rocks]}.')
remainder = (1000000000 - n) % (n - memo[round_rocks])
print(f'Remaining cycles: {remainder}')
for i in range(remainder):
    round_rocks = cycle_rocks(round_rocks)

# print_rocks(round_rocks, cube_rocks, field_length, field_width)

total_load = 0
for pos in round_rocks:
    total_load += field_length - pos[0]

print(f'b: The total load caused by all round rocks after',
      f'1000000000 cycles is {total_load}.')
