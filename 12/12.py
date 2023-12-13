import re

def arrange(sp, gr, debug):
    #pruning    reformulate to single statements. dont forget the gap when pruning
    if debug:
        if len(sp) > 0 and len(gr) > 0:
            if len(sp[0]) < gr[0]: # 1st string too short
                if '#' in sp[0]:
                    return 0
                else:
                    sp = sp[1:]
            elif len(sp[0]) == gr[0] and '#' in sp[0]: # 1st string gud and match len
                sp = sp[1:]
                gr = gr[1:]
                print()
                if len(sp) == len(gr) and all(len(sp[x]) == gr[x] for x in range(len(gr))):
                    print()
                elif not any('?' in x for x in sp) or (len(gr) == 0 and any('#' in x for x in sp)):
                    print()
            # elif sp[0][0] == '#' and len(sp[0])>gr[0]: # 1st string starts gud
            #     if sp[0][gr[0]] == '?': # cut possible
            #         sp[0] = sp[0][gr[0]+1:]
            #         if not sp[0]: # remove slice if empty
            #             sp = sp[1:]
            #         gr = gr[1:]
            #     else:
            #         return 0
                    
            
    # if (len(sp) > 0 and len(gr) > 0 and 
    #     (sp[0][0] == '#'
    #      or not '?' in sp[0][:gr[0]]
    #      or ('#' in sp[0]) and len(sp[0]) <= gr[0])):
    #     if len(sp[0]) == gr[0]:
    #         sp = sp[1:]
    #         gr = gr[1:]
    #     elif len(sp[0]) < gr[0] or sp[0][gr[0]] == '#':
    #         return 0
    #     else:
    #         sp[0] = sp[0][gr[0]:]
    #         gr = gr[1:]
    # if (len(sp) > 0 and len(gr) > 0 and 
    #     (sp[-1][-1] == '#'
    #      or not '?' in sp[-1][-gr[0]:]
    #      or ('#' in sp[-1]) and len(sp[-1]) <= gr[-1])):
    #     if len(sp[-1]) == gr[-1]:
    #         sp = sp[:-1]
    #         gr = gr[:-1]
    #     elif len(sp[-1]) < gr[-1]:
    #         return 0
    #     else:
    #         sp[-1] = sp[-1][:-gr[-1]]
    #         gr = gr[:-1]
    n = 0
    # are we finished?
    if len(sp) == len(gr) and all(len(sp[x]) == gr[x] for x in range(len(gr))):
        return 1
    if not any('?' in x for x in sp) or (len(gr) and any('#' in x for x in sp)) == 0:
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
            
    n += arrange(new_sp_gud, gr, debug)
    n += arrange(new_sp_dmg, gr, debug)    
    
    return n

springs = []
groups = []
with open('12/input.txt') as f:
    for line in f.read().strip().split('\n'):
        a, b = line.split()
        springs.append(re.findall('[?#]+', a))
        groups.append([int(x) for x in b.split(',')])

# arrange(springs[2],groups[2])
# arrange(['?#?#??#??#?', '???????#'], [8, 1, 3, 1, 1])
# arrange(['???#???', '?#??????'], [1, 2, 2, 3, 2], True)
arrange(['???#???', '?#??????'], [1, 2, 2, 3, 2], True)

sum_of_arrangements = 0
for s, g in zip(springs, groups):
    # print(s,g)
    a = arrange(s,g, False)
    b = arrange(s,g, True)
    if a!=b:
        print(a,b)
        print(s,g)
        break
    sum_of_arrangements += a
    # print(a, s, g)

print(sum_of_arrangements) # a:6852
