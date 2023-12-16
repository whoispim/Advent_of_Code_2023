import numpy as np

with open('13/input.txt', 'r') as f:
    notes = []
    for i in f.read().strip().split('\n\n'):
        raw_note = []
        for line in i.split('\n'):
            raw_note.append([1 if x == '#' else 0 for x in line])
        notes.append(np.asarray(raw_note))
        
        
sum_of_pos = 0
for n in notes:
    for i in range(1,n.shape[1]):
        sw = min(i, n.shape[1] -i) # slice width
        if (n[: ,i-sw:i] == n[:, i:i+sw][:,::-1]).all():
            sum_of_pos += i
            break
    for i in range(1,n.shape[0]):
        sw = min(i, n.shape[0] -i)
        if (n[i-sw:i, :] == n[i:i+sw, :][::-1]).all():
            sum_of_pos += i*100
            break
            
print(f'a: The sum of the position of all mirror lines is {sum_of_pos}.')


sum_of_pos = 0
for n in notes:
    for i in range(1,n.shape[1]):
        sw = min(i, n.shape[1] -i) # slice width
        if (n[: ,i-sw:i] == n[:, i:i+sw][:,::-1]).sum() == n.shape[0]*sw-1:
            sum_of_pos += i
            break
    for i in range(1,n.shape[0]):
        sw = min(i, n.shape[0] -i)
        if (n[i-sw:i, :] == n[i:i+sw, :][::-1]).sum() == n.shape[1]*sw-1:
            sum_of_pos += i*100
            break
            
print(f'b: The sum of the position of all dirty mirror lines is {sum_of_pos}.')
