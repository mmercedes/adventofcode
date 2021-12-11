
def get_incomplete_char(line):
    queue = []
    pairs = {")":"(", "}":"{", "]":"[", ">":"<"}
    
    for char in line:
        if char == "\n":
            continue
        if char in pairs.values():
            queue.append(char)
        else:
            if pairs[char] != queue[-1]:
                return char
            else:
                queue.pop(-1)
    return None
    
def p1():
    points = {")":3, "]":57, "}":1197, ">":25137}
    ans = 0
    with open("./inputs/input_10.txt") as f:
        for line in f:
            char = get_incomplete_char(line)
            if char != None:
              ans += points[char]
    return ans

def get_completion_str(line):
    queue = []
    pairs = {")":"(", "}":"{", "]":"[", ">":"<"}
    rpairs = {"(":")", "{":"}", "[":"]", "<":">"}    
    
    for char in line:
        if char == "\n":
            continue
        if char in pairs.values():
            queue.append(char)
        else:
            if pairs[char] != queue[-1]:
                return None
            else:
                queue.pop(-1)

    if len(queue) is 0:
        return None

    return "".join([rpairs[char] for char in queue[::-1]])

def p2():
    points = {")":1, "]":2, "}":3, ">":4}    
    scores = []
    with open("./inputs/input_10.txt") as f:
        for line in f:
            cs = get_completion_str(line)
            if cs != None:
                score = 0
                for c in cs:
                    if c == "\n": continue
                    score *= 5
                    score += points[c]
                scores.append(score)
                
    return sorted(scores)[len(scores)//2]
    
print("p1: %i" % p1())
print("p2: %i" % p2())
