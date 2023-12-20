def gen_work(comparison):
    if '<' in comparison:
        var, val = comparison.split('<')
        def work(part):
            return part[var] < int(val)
    elif '>' in comparison:
        var, val = comparison.split('>')
        def work(part):
            return part[var] > int(val)
    return work

with open('19/input.txt', 'r') as f:
    workflows_raw, parts_raw = f.read().strip().split('\n\n')
    parts = []
    for part in parts_raw.split('\n'):
        ratings_raw = part[1:-1].split(',')
        ratings = {}
        for r in ratings_raw:
            a, b = r.split('=')
            ratings[a] = int(b)
        parts.append(ratings)
    
    workflows = {}
    for flow in workflows_raw.split('\n'):
        name, tasks = flow[:-1].split('{')
        task_list = []
        for task in tasks.split(','):
            if ':' in task: # comparison
                comparison, result = task.split(':')
                if result == 'A' or result == 'R': # A/R -> True/False
                    result = (result == 'A')
                task_list.append([gen_work(comparison), result])
            else: # name of other workflow / A / R
                if task == 'A' or task == 'R':
                    task = (task == 'A')
                task_list.append(task)
            workflows[name] = task_list
    
parts_accepted = []

for part in parts:
    curr_flow = 'in'
    finished = False
    while not finished:
        # print(f'Curent Flow: {curr_flow}')
        for step in workflows[curr_flow]:
            # print(f'  Current Step: {step}')
            if isinstance(step, list):
                if step[0](part):
                    result = step[1]
                else:
                    continue
            else:
                result = step
            if isinstance(result, bool):
                parts_accepted.append(result)
                finished = True
                break
            else:
                curr_flow = result
                break

sum_ratings = 0
for i, hot_or_not in enumerate(parts_accepted):
    if hot_or_not:
        sum_ratings += sum(parts[i].values())

print(f'The sum of XMAS ratings of all accepted parts is {sum_ratings}')
