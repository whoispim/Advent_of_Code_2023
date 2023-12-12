import re

def arrange(sp, gr):
    n = 0
    s = sp
    
    return n, unused_groups

springs = []
groups = []
with open('12/input_t.txt') as f:
    for line in f.read().strip().split('\n'):
        a, b = line.split()
        springs.append(re.findall('[?#]+', a))
        groups.append([int(x) for x in b.split(',')])

print(springs)
print(groups)

print(arrange(springs[0], groups[0]))