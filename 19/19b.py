def gen_work(comparison):
    if '<' in comparison:
        var, val = comparison.split('<')
    elif '>' in comparison:
        var, val = comparison.split('>')
    val = int(val)
    # part will be dict of lists of tuples
    def work(part):
        new_matched = []
        new_unmatched = []
        if '<' in comparison:
            for r in part[var]:
                if r[1] < val:
                    new_matched.append(r)
                elif r[0] >= val:
                    new_unmatched.append(r)
                else:
                    new_matched.append((r[0], val - 1))
                    new_unmatched.append((val, r[1]))
        else:
            for r in part[var]:
                if r[0] > val:
                    new_matched.append(r)
                elif r[1] <= val:
                    new_unmatched.append(r)
                else:
                    new_matched.append((val + 1, r[1]))
                    new_unmatched.append((r[0], val))
        # remove parts with empty ranges
        matched = {}
        unmatched = {}
        if len(new_matched) > 0:
            matched = dict(part)
            matched[var] = new_matched
        if len(new_unmatched) > 0:
            unmatched = dict(part)
            unmatched[var] = new_unmatched
        return matched, unmatched
    return work


def go_with_flow(flow, part):
    if isinstance(flow, bool):
        if flow:
            print('    Accepted!')
            return [part]
        else:
            print('    Rejepted!')
            return []
    print(f'Current Flow: {flow}')
    result = []
    for step in workflows[flow]:
        print(f'  Current Step: {step}')
        if isinstance(step, list):
            matched, unmatched = step[0](part)
            result.extend(go_with_flow(step[1], matched))
            part = unmatched
        else:
            result.extend(go_with_flow(step, part))
    return result
    

with open('19/input.txt', 'r') as f:
    workflows_raw, _parts_raw = f.read().strip().split('\n\n')
    
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
            
super_part = {
    'x': [(1, 4000)],
    'm': [(1, 4000)],
    'a': [(1, 4000)],
    's': [(1, 4000)]
}

final_part = go_with_flow('in', super_part)

# lets hope there is no overlap
rangesum = 0
for part in final_part:
    p = 1
    for rs in part.values():
        n = 0
        for r in rs:
            n += r[1] - r[0] + 1
        p *= n
    rangesum += p

print(f'There are {rangesum} distinct combinations that are accepted',
      f'by the elves\' workflows.')
