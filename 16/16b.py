def encounter(coord, dir, devi):
    next = []
    if devi == '/':
        if dir == 0:
            dir = 3
        elif dir == 1:
            dir = 2
        elif dir == 2:
            dir = 1
        else:
            dir = 0
        next.append((next_coord(coord, dir), dir))
    elif devi == '\\':
        if dir == 0:
            dir = 1
        elif dir == 1:
            dir = 0
        elif dir == 2:
            dir = 3
        else:
            dir = 2
        next.append((next_coord(coord, dir), dir))
    elif (devi == '-' and (dir == 0 or dir == 2)
          or devi == '|' and (dir == 1 or dir == 3)):
        next.append((next_coord(coord, dir), dir))
    else:
        dir_a = (dir + 1) % 4
        dir_b = (dir + 3) % 4
        next.append((next_coord(coord, dir_a), dir_a))
        next.append((next_coord(coord, dir_b), dir_b))
    return next


def next_coord(coord, dir):
    global dir_dict
    return (coord[0] + dir_dict[dir][0], coord[1] + dir_dict[dir][1])


def energize(start, contrap):
    global max_h
    global max_w
    beam = [start]
    energized = set()
    while not len(beam) == 0:
        b = beam.pop(0)
        if (b not in energized
            and 0 <= b[0][0] <= max_h
            and 0 <= b[0][1] <= max_w):
            energized.add(b)
            b_coord, b_dir = b
            if b_coord in contrap:
                beam.extend(
                    encounter(b_coord, b_dir, contrap[b_coord])
                )
            else:
                beam.append((next_coord(b_coord, b_dir), b_dir))
    
    return len(set([x[0] for x in energized]))


with open('16/input.txt','r') as f:
    contrap = {}
    max_h = -1
    for i, line in enumerate(f.read().strip().split('\n')):
        max_h += 1
        for j, x in enumerate(line):
            if x != '.':
                contrap[(i,j)] = x
    max_w = len(line) - 1

# >v<^
# rdlu
# 0123
dir_dict = {
    0: ( 0, 1),
    1: ( 1, 0),
    2: ( 0,-1),
    3: (-1, 0)
    }

start_energy = {}
for i in range(max_w+1):
    start = ((0,i),1)
    start_energy[start] = energize(start, contrap)
    start = ((max_h,i),3)
    start_energy[start] = energize(start, contrap)
for i in range(max_h+1):
    start = ((i,0),0)
    start_energy[start] = energize(start, contrap)
    start = ((i,max_w),2)
    start_energy[start] = energize(start, contrap)

print(f'b: From the best starting position the',
      f'beam energizes {max(start_energy.values())} tiles.')
