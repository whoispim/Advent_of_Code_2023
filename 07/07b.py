def score_hand(cards):
    counts = [cards.count(x) for x in range(1,15)]
    # lets score in 6 digit hexadecimal. this allows us to use the first digit for
    # the type of hand and the remaining 5 for the highest card in each position
    score = 0
    if any(c + counts[0] >= 5 for c in counts[1:]): # five of a kind
        score += 0x600000
    elif any(c + counts[0] >= 4 for c in counts[1:]): # four of a kind
        score += 0x500000
    elif 3 in counts and 2 in counts or counts.count(2) == 2 and counts[0] == 1: # full house
        score += 0x400000
    elif any(c + counts[0] >= 3 for c in counts[1:]): # three of a kind
        score += 0x300000
    elif counts.count(2) == 2: # two pairs
        score += 0x200000
    elif any(c + counts[0] >= 2 for c in counts[1:]): # one pair
        score += 0x100000
    # else high card
    
    for i, card in enumerate(cards):
        score += card * 0x10**(4-i)
        
    return score

if __name__ == '__main__':
    card_dict = {
        str(x): x
        for x in range(2,10)
    } | {'T':10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14} # J is now 1 instead of 11
    with open('07/input.txt', 'r') as f:
        hands = []
        for line in f.read().strip().split('\n'):
            cards, bet = line.split()
            cards = [card_dict[x] for x in cards]
            bet = int(bet)
            hands.append([cards, bet])
    for hand in hands:
        score = score_hand(hand[0])
        hand.append(score)
        
    hands = sorted(hands, key=lambda x: x[2])

    total_bid = sum([hands[i][1] * (i+1) for i in range(len(hands))])
    print(f'b: Total of bid multiplied by rank is {total_bid} if J is a wildcard.')
