with open('11/input_t.txt','r') as f:
    stars = []
    for i, line in enumerate(f.read().strip().split('\n')):
        for j, ch in enumerate(line):
            if ch == '#':
                stars.append([i,j])
max_r = max(x[0] for x in stars)
max_c = max(x[1] for x in stars)
empty_rows = [x for x in range(max_r+1) if x not in [x[0] for x in stars]]
empty_cols = [x for x in range(max_c+1) if x not in [x[1] for x in stars]]
print(stars)
print(empty_rows)
print(empty_cols)
for s in stars:
    for r in reversed(empty_rows):
        if s[0] > r:
            s[0] += 1
    for c in reversed(empty_cols):
        if s[1] > c:
            s[1] += 1


print(stars)