import numpy as np

#          <v^>
con_dic = {
    '|': 0b0110,
    '-': 0b1001,
    'L': 0b0011,
    'J': 0b1010,
    '7': 0b1100,
    'F': 0b0101,
    '.': 0b0000,
    'S': 0b1111
}

with open('10/input.txt', 'r') as f:
    pipes_raw = []
    for line in f.read().strip().split('\n'):
        pipes_raw.append([con_dic[x] for x in line])

pipes = np.asarray(pipes_raw)
pipes = np.pad(pipes, 1)

pos = tuple([x[0] for x in np.where(pipes == 15)])

# figure out first direction (valid neighbour)
if pipes[pos[0], pos[1] + 1] >> 3 & 1: # right
    dir = 0b0001
elif pipes[pos[0] + 1, pos[1]] >> 1 & 1: # down
    dir = 0b0100
else: # its a circle, must be one of the other two -> left
    dir = 0b1000
#              <v^>
dir_to_np = {0b0001: ( 0, 1),
             0b0010: (-1, 0),
             0b0100: ( 1, 0),
             0b1000: ( 0,-1)
}
dir_to_from = {0b0001: 0b1000,
               0b1000: 0b0001,
               0b0010: 0b0100,
               0b0100: 0b0010
}
dir_left_right = {0b0001: (0b0010, 0b0100),
                  0b0010: (0b1000, 0b0001),
                  0b0100: (0b0001, 0b1000),
                  0b1000: (0b0100, 0b0010)
}
n = 0
dist = {pos: 0}
neighbours = {}
while True:
    n += 1
    pos = tuple(np.add(pos, dir_to_np[dir]))
    dist[pos] = n
    neighbours[pos] = [
        tuple(np.add(pos, dir_to_np[dir_left_right[dir][0]])),
        tuple(np.add(pos, dir_to_np[dir_left_right[dir][1]]))
    ]
    dir = pipes[pos] ^ dir_to_from[dir]
    if pipes[pos] == 15:
        break
    
print(f'a: The farthest point is {n//2} steps away from the start.')

# if we circled right, more right neighbours will overlap the path
r = sum(1 for x in neighbours.values() if x[1] in dist.keys())
l = sum(1 for x in neighbours.values() if x[0] in dist.keys())
print(l, r)
if r > l:
    inner_neighbours = [x[1] for x in neighbours.values()]
else:
    inner_neighbours = [x[0] for x in neighbours.values()]
inner_candidates = [x for x in inner_neighbours]
inner_empty = []
while len(inner_candidates) > 0:
    coord = inner_candidates.pop(0)
    if not coord in dist.keys() and not coord in inner_empty:
        inner_empty.append(coord)
        inner_candidates.extend([
            (coord[0], coord[1]+1),
            (coord[0]+1, coord[1]),
            (coord[0], coord[1]-1),
            (coord[0]-1, coord[1])
        ])
# print(inner_empty)
# > 427
print(len(inner_empty))
plot_dict = {v: k for k, v in con_dic.items()}
a=0
for i in range(pipes.shape[0]):
    for j in range(pipes.shape[1]):
        if (i,j) in dist.keys():
            print(plot_dict[pipes[i,j]], end='')
        elif (i,j) in inner_empty:
            print('█', end='')
            a+=1
        else:
            print(' ', end='')
    print(a)

for i in range(pipes.shape[0]):
    for j in range(pipes.shape[1]):
        if (i,j) in dist.keys():
            print(plot_dict[pipes[i,j]], end='')
        elif ((i+1,j) in dist.keys()
              or (i-1,j) in dist.keys()
              or (i,j+1) in dist.keys()
              or (i,j-1) in dist.keys()) and (i,j) not in inner_empty:
            print('█', end='')
        else:
            print(' ', end='')
    print()