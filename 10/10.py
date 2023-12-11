import numpy as np

# beware, i didn't have a lot of time and this is one bowl of spaghetti

def get_neighbours(pos, dir):
    if   dir == 0b0001:
        if   pipes[pos] == 0b1001: return [[(-1,0)],[(1,0)]]
        elif pipes[pos] == 0b1010: return [[],[(1,0),(0,1)]]
        elif pipes[pos] == 0b1100: return [[(-1,0),(0,1)],[]]
    elif dir == 0b0010:
        if   pipes[pos] == 0b0101: return [[(-1,0),(0,-1)],[]]
        elif pipes[pos] == 0b0110: return [[(0,-1)],[(0,1)]]
        elif pipes[pos] == 0b1100: return [[],[(-1,0),(0,1)]]
    elif dir == 0b0100:
        if   pipes[pos] == 0b0011: return [[],[(1,0),(0,-1)]]
        elif pipes[pos] == 0b0110: return [[(0,1)],[(0,-1)]]
        elif pipes[pos] == 0b1010: return [[(1,0),(0,1)],[]]
    elif dir == 0b1000:
        if   pipes[pos] == 0b0011: return [[(-1,0),(0,1)],[]]
        elif pipes[pos] == 0b0101: return [[],[(-1,0),(0,-1)]]
        elif pipes[pos] == 0b1001: return [[(1,0)],[(-1,0)]]
    return [[],[]]


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
neighbours_l = []
neighbours_r = []
while True:
    n += 1
    pos = tuple(np.add(pos, dir_to_np[dir]))
    dist[pos] = n
    lr = get_neighbours(pos, dir)
    neighbours_l.extend([(pos[0]+x[0],pos[1]+x[1]) for x in lr[0]]) 
    neighbours_r.extend([(pos[0]+x[0],pos[1]+x[1]) for x in lr[1]])
    # neighbours[pos] = [
    #     tuple(np.add(pos, dir_to_np[dir_left_right[dir][0]])),
    #     tuple(np.add(pos, dir_to_np[dir_left_right[dir][1]]))
    # ]
    dir = pipes[pos] ^ dir_to_from[dir]
    if pipes[pos] == 15:
        break
    
print(f'a: The farthest point is {n//2} steps away from the start.')

# if we circled right, their will be more left neighbours
r = len(neighbours_r)
l = len(neighbours_l)
# print(l, r)

if r > l:
    inner_neighbours = [x for x in neighbours_l]
else:
    inner_neighbours = [x for x in neighbours_r]
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
        
print(f'b: The total enclosed area is {len(inner_empty)}.')

plot_dict = {0b0110 :"┃",
             0b1001:"━",
             0b0011:"┗",
             0b1010:"┛",
             0b1100:"┓",
             0b0101:"┏",
             0b1111:"S"
}
# a=0
# for i in range(pipes.shape[0]):
#     for j in range(pipes.shape[1]):
#         if (i,j) in dist.keys():
#             print(plot_dict[pipes[i,j]], end='')
#         elif (i,j) in inner_empty:
#             print('█', end='')
#             a+=1
#         else:
#             print('.', end='')
#     print(a)
