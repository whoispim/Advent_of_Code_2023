def part_a(cards):
    total_points = 0
    for card in cards:
        winners = card[0].intersection(card[1])
        if len(winners) > 0:
            total_points += 2**(len(winners)-1)
            
    return total_points


def part_b(cards):
    win_dict = {}
    for i, card in reversed(list(enumerate(cards))):
        n_winners = len(card[0].intersection(card[1]))
        if n_winners == 0:
            win_dict[i+1] = 0
        else:
            win_dict[i+1] = n_winners + sum([win_dict[i+x+2] for x in range(n_winners)])
    n_cards = sum(win_dict.values()) + len(win_dict)
    
    return n_cards


if __name__ == '__main__':
    scratchcards = []
    with open('04/input.txt', 'r') as f:
        for line in f.read().strip().split('\n'):
            num_win, num_have = line.split(' | ')
            scratchcards.append([
                set([int(x) for x in num_win.split()[2:]]),
                set([int(x) for x in num_have.split()]),
                ])
            
    print(f'a: The scratchcards are worth {part_a(scratchcards)} in total.')
    print(f'b: The elf ends up with {part_b(scratchcards)} scratchcards.')
