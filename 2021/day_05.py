#!/usr/bin/env python
import re

def lookup_insert(m, x, y):
    if x not in m:
        m[x] = {}
    if y not in m[x]:
        m[x][y] = 0
    m[x][y] = m[x][y]+1

def insert_line(m, x1, y1, x2, y2):
    dx = 1 if (x1 < x2) else -1
    dy = 1 if (y1 < y2) else -1

    i, j = (x1, y1)
    lookup_insert(m, x2, y2)

    while ((i != x2) or (j != y2)):
        lookup_insert(m, i, j)
        if (i != x2): i += dx
        if (j != y2): j += dy

def day5():
    p1_lookup = {}
    p2_lookup = {}    
    with open("./inputs/input_05.txt") as f:
        for line in f:
            m = re.match(r"(?P<x1>[0-9]+),(?P<y1>[0-9]+) -> (?P<x2>[0-9]+),(?P<y2>[0-9]+)", line).groupdict()
            x1, y1, x2, y2 = (int(m['x1']), int(m['y1']), int(m['x2']), int(m['y2']))
            
            if (x1 == x2) or (y1 == y2):
                insert_line(p1_lookup, x1, y1, x2, y2)
                
            insert_line(p2_lookup, x1, y1, x2, y2)

    p1_ans = 0
    for x in p1_lookup:
        for y in p1_lookup[x]:
            if p1_lookup[x][y] > 1:
                p1_ans += 1

    p2_ans = 0
    for x in p2_lookup:
        for y in p2_lookup[x]:
            if p2_lookup[x][y] > 1:
                p2_ans += 1                

    print("p1 ans: %i" % p1_ans)
    print("p2 ans: %i" % p2_ans)
            
day5()

