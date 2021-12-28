def has_path(graph, src, dst):
    """
    This fuction uses recursive to find a path
    Depth first
    """
    if src == dst: return True
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst):
            return True
        
    return False

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph, 'f', 'k')) # True
