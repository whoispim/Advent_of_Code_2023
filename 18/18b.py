class WeNeverHadAZeroAfterTheDecimalPoint(Exception):
    pass

with open('18/input.txt', 'r') as f:
    instructions = []
    for line in [x.split()[2] for x in f.read().strip().split('\n')]:
        direction = int(line[7])
        distance = int(line[2:7], 16)
        instructions.append((direction, distance))
        
dir_dict = {
    0: ( 0, 1),
    1: ( 1, 0),
    2: ( 0,-1),
    3: (-1, 0)
    }

dug_corners = [(0,0)]
border_length = 0

for inst in instructions:
    pos_dif = dir_dict[inst[0]]
    new_corner = (dug_corners[-1][0] + pos_dif[0] * inst[1],
                    dug_corners[-1][1] + pos_dif[1] * inst[1])
    dug_corners.append(new_corner)
    border_length += inst[1]

# shoelace formula
lagoon = 0
for i in range(len(dug_corners) -1):
    a = dug_corners[i]
    b = dug_corners[i + 1]
    lagoon += a[0]*b[1] - a[1]*b[0]
# above value / 2 plus the other half of each border square
# plus one because 4 more inside corners than outside ones
lagoon = abs(lagoon) / 2 + border_length / 2 + 1

if lagoon%1 != 0:
    raise WeNeverHadAZeroAfterTheDecimalPoint
else:
    lagoon = int(lagoon)

print(f'b: Total size of the dug out lagoon: ',
      f'with real instructions: {lagoon}')
