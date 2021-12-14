import sys

def read_input():
    polymer = None
    pmap = {}
    with open("./inputs/input_14.txt") as f:
        for line in f:
            if polymer is None:
                polymer = line.strip()
            elif not line.strip():
                continue
            else:
                key, val = line.split("->")
                pmap[key.strip()] = val.strip()

    return (polymer, pmap)

"""
# slow version that only worked for part 1
def run_sim(steps):
    polymer, pmap = read_input()

    for step in range(steps):
        print("step %i" % step)
        new_polymer = ""
        for i in range(len(polymer)-1):
            pair = polymer[i:i+2]
            c = pmap.get(pair, '')
            new_polymer += pair[0] + c
            
        new_polymer += polymer[-1]
        polymer = new_polymer

    counts = {}
    for c in polymer:
        if c not in counts:
            counts[c] = 0
        counts[c] = counts[c]+1

    most, least = 0, sys.maxsize
    for x in counts.values():
        if x > most: most = x
        if x < least: least = x

    return most-least
"""

def run_sim(steps):
    polymer, pmap = read_input()

    pairs, counts = {}, {}
    for i in range(len(polymer)-1):
        pair = polymer[i:i+2]
        element = polymer[i]
        
        if pair not in pairs: pairs[pair] = 0
        if element not in counts: counts[element] = 0
        
        pairs[pair] += 1
        counts[element] += 1
        
    last = polymer[-1]
    if last not in counts: counts[last] = 0
    counts[last] += 1

    for _ in range(steps):
        for pair,count in list(pairs.items()):
            element = pmap.get(pair, "")
            pairs[pair] -= count
            if element != "": counts[element] += count
            if pair[0]+element not in pairs: pairs[pair[0]+element] = 0
            if element+pair[1] not in pairs: pairs[element+pair[1]] = 0            
            pairs[pair[0]+element] += count
            pairs[element+pair[1]] += count
    
    most, least = 0, sys.maxsize
    for x in counts.values():
        if x > most: most = x
        if x < least: least = x

    return most-least

print("p1: %i" % run_sim(10))
print("p2: %i" % run_sim(40))
