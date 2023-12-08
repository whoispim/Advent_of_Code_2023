from math import lcm

with open('08/input.txt', 'r') as f:
    instructions, maps = f.read().strip().split('\n\n')
    instructions = [0 if x == 'L' else 1 for x in instructions]
    maps = {x[:3]: [x[7:10], x[12:15]] for x in maps.split('\n')}

positions = [x for x in maps if x[2] == 'A']
a_to_z = []
z_to_z = []
for i in range(len(positions)):
    moves = 0
    while not positions[i][2] == 'Z':
        positions[i] = maps[positions[i]][instructions[moves%len(instructions)]]
        moves += 1
    a_to_z.append(moves)
    
    positions[i] = maps[positions[i]][instructions[moves%len(instructions)]]
    moves += 1
    new_moves = 1
    while not positions[i][2] == 'Z':
        positions[i] = maps[positions[i]][instructions[moves%len(instructions)]]
        moves += 1
        new_moves += 1
    z_to_z.append(new_moves)
# print(a_to_z)
# print(z_to_z)
# ...why are a_to_z and z_to_z the same..? well, that makes it easier
least_common_multiple = lcm(*a_to_z)

print(f'It takes {least_common_multiple} moves until all {len(positions)} ghosts',
      f'arrive at a ..Z position at the same time.')
