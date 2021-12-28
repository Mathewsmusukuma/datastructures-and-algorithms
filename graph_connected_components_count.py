def connected_components_count(graph):
    vistited = set()
    count = 0
    for node in graph:
        if explore(graph, node, vistited):
            count += 1
    return count


def explore(graph, current, visited):
    if current in visited: return False

    visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)
    
    return True

# Run the function
connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 2
