
def read_graph():
    graph = {}
    with open("./inputs/input_12.txt") as f:
        for line in f:
            a,b = line.strip().split("-")
            if a not in graph:
                graph[a] = set()
            if b not in graph:
                graph[b] = set()
                
            graph[a].add(b)
            graph[b].add(a)
    return graph

def is_valid_path(path, is_p2):
    if not is_p2:
        for stop in path:
            if stop.islower() and path.count(stop) > 1:
                return False
    else:
        if path.count("start") > 1:
            return False
        small_path_seen = None
        for stop in path:
            if stop.islower():
                if path.count(stop) > 2:
                    return False
                elif path.count(stop) == 2:
                    if small_path_seen is not None and small_path_seen != stop:
                        return False
                    small_path_seen = stop
    return True
    

def generate_paths(graph, paths, is_p2=False, previous=['start']):
    start = previous[-1]
    if start == 'end':
        paths.append(previous)
        return

    if len(graph[start]) == 0:
        return

    for stop in graph[start]:
        new_path = previous.copy()
        new_path.append(stop)
        if is_valid_path(new_path, is_p2):
            generate_paths(graph, paths, is_p2, new_path)
    return

def day12():
    graph = read_graph()
    paths_p1 = []
    paths_p2 = []
    generate_paths(graph, paths_p1)
    generate_paths(graph, paths_p2, True)    
    print("p1: %i" % len(paths_p1))
    print("p2: %i" % len(paths_p2))

day12()
