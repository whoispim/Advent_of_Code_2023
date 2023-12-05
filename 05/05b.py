def seeds_to_loc(seeds, maps):
    locations = []
    for seedrange in seeds:
        cur_ranges = [seedrange]
        for s_map in maps:
            new_ranges = []
            for rang in cur_ranges:
                mapped = apply_map(rang, s_map)
                new_ranges.extend(mapped)
            cur_ranges = new_ranges
        locations.extend(cur_ranges)
    return min([x[0] for x in locations])


def apply_map(r, m):
    mapd = []
    unmapd = [r]
    for line in m:
        mapdiff = line[0] - line[1] 
        new_unmapd = []
        while len(unmapd) > 0:
            ra = unmapd.pop(0)
            m_s = line[1]
            m_e = line[1] + line[2] - 1
            if m_s <= ra[0] and ra[1] <= m_e: # completely inside map
                mapd.append((ra[0] + mapdiff,
                             ra[1] + mapdiff))
            elif m_s <= ra[0] <= m_e and m_e < ra[1]: # overlaps map on right side
                mapd.append((ra[0] + mapdiff,
                             m_e  + mapdiff))
                new_unmapd.append((m_e + 1,
                                   ra[1]))
            elif ra[0] < m_s and m_s <= ra[1] <= m_e: # overlaps map on left side
                mapd.append((m_s  + mapdiff,
                             ra[1] + mapdiff))
                new_unmapd.append((ra[0],
                                   m_s - 1))
            elif ra[0] < m_s and m_e < ra[1]: # overlaps map on both sides
                mapd.append((m_s  + mapdiff,
                             m_e + mapdiff))
                new_unmapd.append((ra[0],
                                   m_s - 1))
                new_unmapd.append((m_e + 1,
                                   ra[1]))
            elif ra[1] < m_s or m_e < ra[0]: # does not overlap map
                new_unmapd.append(ra)
            else:
                print('oh no.')
        unmapd = new_unmapd
    # everything unmapped remains unchanged
    return mapd + unmapd


if __name__ == '__main__':
    with open('05/input.txt', 'r') as f:
        seeds_raw = [int(x) for x in f.readline().strip().split(' ')[1:]]
        seeds = []
        for i in range(0,len(seeds_raw),2):
            seeds.append((seeds_raw[i], seeds_raw[i]+seeds_raw[i+1]-1))
        maps = []
        for s_map in f.read().strip().split('\n\n'):
            new_map = []
            for line in s_map.split('\n')[1:]:
                new_map.append(tuple([int(x) for x in line.split()]))
            maps.append(new_map)
    
    location = seeds_to_loc(seeds, maps)
    print(f'b: The closest location is {location}.')
