def validate_part_number(lines):
    if any((not char.isnumeric() and char != '.') for char in ''.join(lines)):
        return True
    return False

def is_part_of_gear(lines):
    for ih, line in enumerate(lines):
        for jh, c in enumerate(line[::-1]):
            if c == '*':
                return True, (ih-1, -jh)
    return False, (0,0)

def part_ab(schem):
    part_numbers = []
    gear_numbers = []
    for i, row in enumerate(schem):
        curr_num = ''
        col_min = sch_w
        for j, col in enumerate(row):
            if col.isnumeric():
                curr_num += col
                col_min = min(col_min,j)
            else:
                if curr_num != '':
                    if validate_part_number([a[col_min-1:j+1] for a in schem[i-1:i+2]]):
                        part_numbers.append(int(curr_num))
                    gearpart = is_part_of_gear([a[col_min-1:j+1] for a in schem[i-1:i+2]])
                    if gearpart[0]:
                        gear_numbers.append([(i+gearpart[1][0],j+gearpart[1][1]), int(curr_num)])
                    curr_num = ''
                    col_min = sch_w
    return part_numbers, gear_numbers


if __name__ == '__main__':                
    with open('03/input.txt', 'r') as f:        
        schematic = f.read().strip().split('\n')

    sch_h = len(schematic)
    sch_w = len(schematic[0])

    schematic.insert(0, '.' * sch_w)
    schematic.append('.' * sch_w)
    schematic = ['.' + row + '.' for row in schematic]

    numbers_a, numbers_b = part_ab(schematic) 
    print(f'The sum of all valid part numbers is {sum(numbers_a)}.')
    
    # part b is very much hacked, sorry 'bout that
    numdict_b = {a: [] for a in set(x[0] for x in numbers_b)}
    
    for a in numbers_b:
        numdict_b[a[0]].append(a[1])
    result_b = 0
    for d in numdict_b:
        print(d, numdict_b[d])
        if len(numdict_b[d])>1:
            result_b += numdict_b[d][0] * numdict_b[d][1]

    print(f'The sum of all gear ratios is {result_b}.')
    