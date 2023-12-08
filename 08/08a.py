with open('08/input.txt', 'r') as f:
    instructions, maps = f.read().strip().split('\n\n')
    instructions = [0 if x == 'L' else 1 for x in instructions]
    maps = {x[:3]: [x[7:10], x[12:15]] for x in maps.split('\n')}

position = 'AAA'
moves = 0

while position != 'ZZZ':
    position = maps[position][instructions[moves%len(instructions)]]
    moves += 1

print(f'It takes {moves} moves to go from AAA to ZZZ.')
