def extra(hist, forward):
    # print(hist)
    new_hist = [hist[x+1]-hist[x] for x in range(len(hist)-1)]
    if new_hist.count(new_hist[0]) == len(new_hist): # check if all are same
        # print(new_hist)
        return new_hist[0]
    else:
        if forward:
            return new_hist[-1] + extra(new_hist, forward)
        else:
            return new_hist[0] - extra(new_hist, forward)
        


with open('09/input.txt', 'r') as f:
    hist_list = [list(map(int,x.split()))
                 for x in f.read().strip().split('\n')]

next_value_sum = 0
for histo in hist_list:
    next_delta = extra(histo, True)
    # print(next_delta, histo[-1] + next_delta)
    next_value_sum += histo[-1] + next_delta
    
print(f'a: The sum of the extrapolated next values is {next_value_sum}.')

previous_value_sum = 0
for histo in hist_list:
    next_delta = extra(histo, False)
    # print(next_delta, histo[0] - next_delta)
    previous_value_sum += histo[0] - next_delta
    
print(f'b: The sum of the extrapolated previous values is {previous_value_sum}.')
    