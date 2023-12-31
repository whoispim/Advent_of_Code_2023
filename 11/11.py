def expand_universe(stars, distance):
    max_r = max(x[0] for x in stars)
    max_c = max(x[1] for x in stars)
    empty_rows = [x for x in range(max_r+1) if x not in [x[0] for x in stars]]
    empty_cols = [x for x in range(max_c+1) if x not in [x[1] for x in stars]]
    
    new_stars = [x.copy() for x in stars]
    for s in new_stars:
        for r in reversed(empty_rows):
            if s[0] > r:
                s[0] += distance
        for c in reversed(empty_cols):
            if s[1] > c:
                s[1] += distance
    return new_stars


def calc_distance(stars_exp):
    sum_dist = 0
    for i, s_a in enumerate(stars_exp):
        for s_b in stars_exp[i+1:]:
            sum_dist += abs(s_a[0]-s_b[0]) + abs(s_a[1]-s_b[1])
    return sum_dist


if __name__ == '__main__':
    with open('11/input.txt','r') as f:
        stars_in = []
        for i, line in enumerate(f.read().strip().split('\n')):
            for j, ch in enumerate(line):
                if ch == '#':
                    stars_in.append([i,j])

    stars_exp = expand_universe(stars_in, 1)
    print(f'a: The sum of the distance between all',
        f'stars is {calc_distance(stars_exp)} after expansion by 1.')

    stars_exp = expand_universe(stars_in, 999999)        
    print(f'b: The sum of the distance between all',
        f'stars is {calc_distance(stars_exp)} after expansion by 999999.')
