with open('18/input.txt', 'r') as f:
    instructions = []
    for line in f.read().strip().split('\n'):
        direction, distance, _color = line.split()
        instructions.append((direction, int(distance)))
        
dir_dict = {
    'R': ( 0, 1),
    'D': ( 1, 0),
    'L': ( 0,-1),
    'U': (-1, 0)
    }

# print(instructions)
pos = (0,0)
dug = [(0,0)]
in_out_walls = [(0,0)]
last_dir = 'U'
for inst in instructions:
    pos_dif = dir_dict[inst[0]]
    for n in range(inst[1]):
        pos = (pos[0] + pos_dif[0], pos[1] + pos_dif[1])
        dug.append(pos)
        if inst[0] == 'U' or inst[0] == 'D':
            if last_dir != inst[0]:
                _ = in_out_walls.pop()
                last_dir = inst[0]
            in_out_walls.append(pos)
if in_out_walls[-1] == (0,0):
    _ = in_out_walls.pop()

# print(dug)
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

print(f'a: Total size of the dug out lagoon: {len(lagoon)}')
