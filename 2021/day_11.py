p1_ans = 0

def read_matrix():
    matrix = []
    with open("./inputs/input_11.txt") as f:
        for line in f:
            matrix.append([int(char) for char in line if char != "\n"])
    return matrix

def flash(f, m, i, j, inc=True):
    if inc:
        m[i][j] = m[i][j]+1
    
    global p1_ans
    flashed = f[i][j]
    if flashed:
        return
    
    if m[i][j] > 9:
        h = len(m)
        w = len(m[0])
        f[i][j] = 1
        p1_ans += 1
        
        if i > 0:
            # left
            flash(f, m, i-1, j)
            # up-left diag
            if j > 0:
                flash(f, m, i-1, j-1)
            # down-left diag
            if j < w-1:
                flash(f, m, i-1, j+1)
        if i < h-1:
            # right
            flash(f, m, i+1, j)
            # up-right diag
            if j > 0:
                flash(f, m, i+1, j-1)
            # down-right diag
            if j < w-1: 
                flash(f, m, i+1, j+1)
        if j > 0:
            # up
            flash(f, m, i, j-1)
        if j < w-1:
            # down
            flash(f, m, i, j+1)

def day11():
    global p2_ans
    m = read_matrix()
    height = len(m)
    width = len(m[0])
    step = 1
    
    while(True):
        if step == 101:
            print("p1: %i" % p1_ans)
        
        flashed = [[0 for i in range(width)] for j in range(height)]
        # add 1 to energy
        for i in range(height):
            for j in range(width):
                m[i][j] = m[i][j]+1
        
        # trigger flashes
        for i in range(height):
            for j in range(width):
                flash(flashed, m, i, j, False)

        # check if sync'd
        all_flashed = True
        for i in range(height):
            for j in range(width):
                if flashed[i][j] != 1: all_flashed = False
        if all_flashed:
            print("p2: %i" % step)
            return

        # reset energy levels
        for i in range(height):
            for j in range(width):
                if flashed[i][j]:
                    m[i][j] = 0
        step+=1
    return

day11()

