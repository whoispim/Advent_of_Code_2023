def gen_work(comparison):
    if '<' in comparison:
        var, val = comparison.split('<')
        def work(part):
            return part[var] < val
    elif '>' in comparison:
        var, val = comparison.split('>')
        def work(part):
            return part[var] > val
    return work

with open('19/input_t.txt', 'r') as f:
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
    
        
print(parts)
print(workflows)
# workflows['px'][0][0](part[0])