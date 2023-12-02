def part_a(games):
    limit = {
        'r': 12,
        'g': 13,
        'b': 14
    }
        
    valid_sum = 0
    for i, game in enumerate(games):
        valid = True
        for pull in game:
            for col in pull:
                if pull[col] > limit[col]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            valid_sum += i+1
    
    return valid_sum
    
    
def part_b(games):
    power_sum = 0
    for i, game in enumerate(games):
        col_max = {
            'r': 0,
            'g': 0,
            'b': 0
        }
        for pull in game:
            for col in pull:
                if pull[col] > col_max[col]:
                    col_max[col] = pull[col]
        power_sum += col_max['r'] * col_max['b'] * col_max['g']
    
    return power_sum
    
    
if __name__ == '__main__':
    games = []
    with open('02/input.txt', 'r') as f:
        for line in f.read().strip().split('\n'):
            pulls = line.split(': ', 1)[1].split('; ')
            game = []
            for pull in pulls:
                p = {}
                for balls in pull.split(', '):
                    num, col = balls.split(' ')
                    p[col[0]] = int(num)
                game.append(p)
            games.append(game)
            
    print(f'The sum of the number of all valid games is {part_a(games)}.')
    print(f'The sum of power of the minimum number of balls per color in each game is {part_b(games)}.')
