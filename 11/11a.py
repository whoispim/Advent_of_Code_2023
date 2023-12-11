with open('11/input.txt','r') as f:
    stars = []
    for i, line in enumerate(f.read().strip().split('\n')):
        for j, ch in enumerate(line):
            if ch == '#':
                stars.append([i,j])
max_r = max(x[0] for x in stars)
max_c = max(x[1] for x in stars)
empty_rows = [x for x in range(max_r+1) if x not in [x[0] for x in stars]]
empty_cols = [x for x in range(max_c+1) if x not in [x[1] for x in stars]]

for s in stars:
    for r in reversed(empty_rows):
        if s[0] > r:
            s[0] += 1
    for c in reversed(empty_cols):
        if s[1] > c:
            s[1] += 1

sum_dist = 0
for i, s_a in enumerate(stars):
    for s_b in stars[i+1:]:
        sum_dist += abs(s_a[0]-s_b[0]) + abs(s_a[1]-s_b[1])
        
print(f'a: The sum of the distance between all',
      f'stars is {sum_dist} after expansion by 1.')
