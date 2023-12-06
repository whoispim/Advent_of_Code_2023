import math

def lets_race(races):
    win_ranges = []
    for race in races:
        # approach from bottom
        for t in range(1, race[0]):
            d = (race[0] - t) * t
            if d > race[1]:
                win_start = t
                break
        # approach from top
        for t in reversed(list(range(1, race[0]))):
            d = (race[0] - t) * t
            if d > race[1]:
                win_end = t
                break
        win_ranges.append((win_start, win_end))
    return win_ranges


def lets_race_with_math(races):
    win_ranges = []
    for race in races:
        win_start = race[0]/2-math.sqrt(race[0]**2/4-race[1])
        win_start = math.ceil(win_start)
        win_end = race[0]/2+math.sqrt(race[0]**2/4-race[1])
        win_end = math.floor(win_end)
        print(win_start, win_end)
        win_ranges.append((win_start, win_end))
    return win_ranges
        

if __name__ =='__main__':
    with open('06/input.txt', 'r') as f:
        t = [int(x) for x in f.readline().strip().split()[1:]]
        d = [int(x) for x in f.readline().strip().split()[1:]]
        races = list(zip(t, d))

    win_ranges = lets_race_with_math(races)
    product_win_ranges = 1
    for r in win_ranges:
        product_win_ranges *= r[1] - r[0] + 1
    print(f'a: The product of the amount of possibilities to win per race is {product_win_ranges}.')

    t = ''
    d = ''
    for race in races:
        t += str(race[0])
        d += str(race[1])
    thegreatrace = (int(t), int(d))
    great_win = lets_race_with_math([thegreatrace])
    print(f'b: There are {great_win[0][1] - great_win[0][0] + 1} different strategies to win the great race.')
