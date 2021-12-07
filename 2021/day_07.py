fibs = []

def p1_distance_function(p1, p2):
    return abs(p1-p2)

def p2_distance_function(p1, p2):
    return fibs[abs(p1-p2)]

def generate_fibs(n):
    if len(fibs) >= n:
        return
    total = 0
    for i in range(0, n+1):
        total += i
        fibs.append(total)
    
def crab_game(df):
    with open("./inputs/input_07.txt") as f:
        firstline = f.readline().rstrip()

    poseetions = [int(x) for x in firstline.split(",")]
    start, end = min(poseetions), max(poseetions)
    min_fuel = None
    generate_fibs(end)
    
    for i in range(start, end+1):
        fuel = sum([df(x, i) for x in poseetions])
        if min_fuel is None or fuel < min_fuel:
            min_fuel = fuel

    return min_fuel

print("p1: %i" % crab_game(p1_distance_function))
print("p2: %i" % crab_game(p2_distance_function))
