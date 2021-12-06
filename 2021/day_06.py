
"""
## slow version that only worked for part 1

def fishspawner(days):
    with open("./inputs/input_06.txt") as f:
        firstline = f.readline().rstrip()

    fish = [int(x) for x in firstline.split(",")]
    for i in range(0, days):
        newfish = []
        for f in fish:
            if (f == 0):
                newfish.append(6)
                newfish.append(8)
            else:
                newfish.append(f-1)
        fish = newfish
    return len(fish)

print("part1: %i" % fishspawner(80))
print("part2: %i" % fishspawner(256))
"""

def fast_spawner(days):
    with open("./inputs/input_06.txt") as f:
        firstline = f.readline().rstrip()

    fish = [int(x) for x in firstline.split(",")]
    fd = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    # initalize the inital fish spawn counts
    for f in fish:
        fd[f] = fd[f]+1

    for i in range(0, days):
        # unroll the loop since we know f ranges from 0-8
        f0,f1,f2,f3,f4,f5,f6,f7,f8 = (fd[0],fd[1],fd[2],fd[3],fd[4],fd[5],fd[6],fd[7],fd[8])
        # set newly spawned fish to count of current fish at 0 days
        fd[8] = f0
        # add count of fish at 0 days left to f6 to symbolize reset
        fd[6] = f7 + f0

        fd[7],fd[5],fd[4],fd[3],fd[2],fd[1],fd[0] = (f8,f6,f5,f4,f3,f2,f1)

    return sum(fd.values())

print("part1: %i" % fast_spawner(80))
print("part1: %i" % fast_spawner(256))
