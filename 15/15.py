def hash(snip):
    h = 0
    for s in snip:
        h = ((h + ord(s)) * 17) % 256
    return h


class a_box:
    def __init__(self):
        self.lenses = []
        self.foci = []
    
    def insert_lens(self, label, foc_len):
        try:
            pos = self.lenses.index(label)
            self.foci[pos] = foc_len
        except ValueError:
            self.lenses.append(label)
            self.foci.append(foc_len)
    
    def remove_lens(self, label):
        try:
            pos = self.lenses.index(label)
            self.lenses.pop(pos)
            self.foci.pop(pos)
        except ValueError:
            pass
    
    def __str__(self):
        return str(list(zip(self.lenses, self.foci)))
    
    @property
    def power(self):
        pow = 0
        for i, f in enumerate(self.foci):
            pow += (i+1)*f
        return pow


with open('15/input.txt','r') as f:
    snippets = [x for x in f.read().strip().split(',')]

sum_of_hashs = 0
for snip in snippets:
    sum_of_hashs += hash(snip)
print(f'a: The sum of all hashs is {sum_of_hashs}.')

boxes = [a_box() for x in range(256)]
for snip in snippets:
    if snip[-1] == '-':
        box_num = hash(snip[:-1])
        boxes[box_num].remove_lens(snip[:-1])
    else:
        sep = snip.find('=')
        box_num = hash(snip[:sep])
        boxes[box_num].insert_lens(snip[:sep], int(snip[sep+1:]))
        
total_power = 0
for i, box in enumerate(boxes):
    total_power += (i+1) * box.power

print(f'b: The TOTAL FOCUSING POWER is {total_power}.')
