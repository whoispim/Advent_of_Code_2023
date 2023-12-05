def seeds_to_loc(seeds, maps):
    locations = []
    for seed in seeds:
        curr_num = seed
        for s_map in maps:
            for line in s_map:
            # print(f'valid range: {line[1]} - {line[1]+line[2]-1}', end='')
                if line[1] <= curr_num <= line[1]+line[2]-1:
                    curr_num = line[0] + curr_num - line[1]
                    break
        locations.append(curr_num)
    return min(locations)


if __name__ == '__main__':
    with open('05/input.txt', 'r') as f:
        seeds = [int(x) for x in f.readline().strip().split(' ')[1:]]
        maps = []
        for s_map in f.read().strip().split('\n\n'):
            new_map = []
            for line in s_map.split('\n')[1:]:
                new_map.append(tuple([int(x) for x in line.split()]))
            maps.append(new_map)

    location = seeds_to_loc(seeds, maps)
    print(f'a: The closest location is {location}.')
