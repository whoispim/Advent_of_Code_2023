def lets_race(races):
    win_ranges = []
    for race in races:
        # approach from bottom
        for t in range(1, race[0]):
            d = (race[0] - t) * t
            if d > race[1]:
                win_start = (t, d)
                break
        # approach from top
        for t in reversed(list(range(1, race[0]))):
            d = (race[0] - t) * t
            if d > race[1]:
                win_end = (t, d)
                break
        win_ranges.append((win_start, win_end))
    return win_ranges

if __name__ =='__main__':
    with open('06/input.txt', 'r') as f:
        t = [int(x) for x in f.readline().strip().split()[1:]]
        d = [int(x) for x in f.readline().strip().split()[1:]]
        races = list(zip(t, d))

    win_ranges = lets_race(races)
    product_win_ranges = 1
    for r in win_ranges:
        product_win_ranges *= r[1][0] - r[0][0] + 1
    print(f'a: The product of the amount of possibilities to win per race is {product_win_ranges}.')

    t = ''
    d = ''
    for race in races:
        t += str(race[0])
        d += str(race[1])
    thegreatrace = (int(t), int(d))
    great_win = lets_race([thegreatrace])
    print(f'b: There are {great_win[0][1][0] - great_win[0][0][0] + 1} different strategies to win the great race.')
