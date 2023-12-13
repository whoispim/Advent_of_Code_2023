import re

def arrange(sp, gr):
    #pruning    reformulate to single statements. dont forget the gap when pruning
    if (len(sp) > 0 and len(gr) > 0 and 
        (sp[0][0] == '#'
         or not '?' in sp[0][:gr[0]]
         or ('#' in sp[0]) and len(sp[0]) <= gr[0])):
        if len(sp[0]) == gr[0]:
            sp = sp[1:]
            gr = gr[1:]
        elif len(sp[0]) < gr[0] or sp[0][gr[0]] == '#':
            return 0
        else:
            sp[0] = sp[0][gr[0]:]
            gr = gr[1:]
    if (len(sp) > 0 and len(gr) > 0 and 
        (sp[-1][-1] == '#'
         or not '?' in sp[-1][-gr[0]:]
         or ('#' in sp[-1]) and len(sp[-1]) <= gr[-1])):
        if len(sp[-1]) == gr[-1]:
            sp = sp[:-1]
            gr = gr[:-1]
        elif len(sp[-1]) < gr[-1]:
            return 0
        else:
            sp[-1] = sp[-1][:-gr[-1]]
            gr = gr[:-1]
    # if len(sp) > 0 and len(gr) > 0 and not '?' in sp[-1]:
    #     if len(sp[-1]) == gr[-1]:
    #         sp = sp[:-1]
    #         gr = gr[:-1]
    #     else:
    #         return 0
    n = 0
    # are we finished?
    if len(sp) == len(gr) and all(len(sp[x]) == gr[x] for x in range(len(gr))):
        return 1
    if not any('?' in x for x in sp) or len(gr) == 0:
        return 0
    # find and work only on first '?'
    new_sp_gud = []
    new_sp_dmg = []
    for i, s in enumerate(sp):
        pos = s.find('?')
        if not pos == -1:
            new_sp_gud.append(s[:pos] + '#' + s[pos+1:])
            new_sp_dmg.extend(x for x in [s[:pos], s[pos+1:]] if x) # filter empty slices
            new_sp_gud.extend(sp[i+1:])
            new_sp_dmg.extend(sp[i+1:])
            break
        else:
            new_sp_gud.append(s)
            new_sp_dmg.append(s)
            
    n += arrange(new_sp_gud, gr)
    n += arrange(new_sp_dmg, gr)    
    
    return n

springs = []
groups = []
with open('12/input.txt') as f:
    for line in f.read().strip().split('\n'):
        a, b = line.split()
        springs.append(re.findall('[?#]+', a))
        groups.append([int(x) for x in b.split(',')])

# arrange(springs[2],groups[2])
arrange(['?#?#??#??#?', '???????#'], [8, 1, 3, 1, 1])
sum_of_arrangements = 0
# for s, g in zip(springs, groups):
#     print(s,g)
#     a = arrange(s,g)
#     sum_of_arrangements += a
#     # print(a, s, g)

print(sum_of_arrangements)
