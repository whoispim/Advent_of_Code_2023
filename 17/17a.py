from queue import PriorityQueue
import numpy as np


def next_steps(heatloss, pos, steps_in_line, d):
    global city
    dir_dict = {
        0: ( 0, 1),
        1: ( 1, 0),
        2: ( 0,-1),
        3: (-1, 0)
        }
    
    next = []
    for new_d in [(d+1)%4, (d+3)%4, d]:
        new_pos = (pos[0]+dir_dict[new_d][0], pos[1]+dir_dict[new_d][1])
        new_heat = heatloss + city[new_pos]
        if new_d != d:
            next.append((new_heat, new_pos, 1, new_d))
        elif steps_in_line < 3:
            next.append((new_heat, new_pos, steps_in_line + 1, new_d))
    return next


city = np.genfromtxt('17/input.txt', delimiter=1, dtype=int)
city = np.pad(city, pad_width=1, mode='constant', constant_values=999)
# print(city)

start = (1,1)
goal = (city.shape[0] - 2, city.shape[1] - 2)
# (position, steps in a straight line, direction): energy
heat_dict = {(start, 0, 0): 0}
source_dict = {}

queue = PriorityQueue()
# (energy, position, steps in a straight line, direction)
queue.put((0, start, 0, 0))

while not queue.empty():
    state = queue.get()
    if state[1] == goal:
        goal_key = state[1:]
        break
    next = next_steps(*state)
    for n in next:
        if not n[1:] in heat_dict or heat_dict[n[1:]] > n[0]:
            heat_dict[n[1:]] = n[0]
            queue.put(n)
            source_dict[n[1:]] = state[1:]

visited = []
pos_key = goal_key
while True:
    visited.append(pos_key[0])
    if pos_key[0] == start:
        break
    pos_key = source_dict[pos_key]
    
# print(visited)
for i in range(1,city.shape[0]-1):
    for j in range(1,city.shape[1]-1):
        if (i, j) in visited:
            print('█', end='')
        else:
            print(city[(i,j)], end='')
    print()

print(f'The minimum heat loss the lava can incur is {heat_dict[goal_key]}.')
