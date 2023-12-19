with open('18/input_t.txt', 'r') as f:
    instructions = []
    for line in f.read().strip().split('\n'):
        direction = int(line[11])
        distance = int(line[6:11], 16)
        instructions.append((direction, distance))
        
dir_dict = {
    0: ( 0, 1),
    1: ( 1, 0),
    2: ( 0,-1),
    3: (-1, 0)
    }

print(instructions)

dug_corners = [(0,0)]

for inst in instructions:
    pos_dif = dir_dict[inst[0]]
    new_corner = (dug_corners[-1][0] + pos_dif[0] * inst[1],
                    dug_corners[-1][1] + pos_dif[1] * inst[1])
    dug_corners.append(new_corner)
print(dug_corners)

# shoelace formula
lagoon = 0
for i in range(len(dug_corners) -1):
    a = dug_corners[i]
    b = dug_corners[i + 1]
    print(a,'|||',b, '---->', a[0]*b[1] - a[1]*b[0] )
    lagoon += a[0]*b[1] - a[1]*b[0]
lagoon = abs(lagoon)
print(lagoon)
# way too much
exit()
print(dug)
ij_min = (min(x[0] for x in dug), min(x[1] for x in dug))
ij_max = (max(x[0] for x in dug), max(x[1] for x in dug))

lagoon = set(dug)
we_in = False
for i in range(ij_min[0], ij_max[0]+1):
    for j in range(ij_min[1], ij_max[1]+1):
        if (i, j) in in_out_walls:
            we_in = not we_in
        elif we_in:
            lagoon.add((i, j))

# for i in range(ij_min[0], ij_max[0]+1):
#     for j in range(ij_min[1], ij_max[1]+1):
#         if (i, j) in lagoon:
#             print('█', end='')
#         elif (i, j) in in_out_walls:
#             print('O', end='')
#         elif (i, j) in dug:
#             print('#', end='')
#         else:
#             print('.', end='')
#     print()

print(f'Total size of the dug out lagoon: {len(lagoon)}')