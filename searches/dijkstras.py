from functools import reduce

def dijkstras(weighted_graph,src,dst):

    vertices = set()
    dist = {}
    prev = {}
    
    # add all vertices to set
    for vertex in weighted_graph.vertices:
        vertices.add(vertex)
        dist[vertex] = float('inf')
        prev[vertex] = None

    dist[src] = 0

    while vertices:
        min_dist_node = min(list(filter(lambda x: x[0] in vertices,dist.items())),key=lambda x: x[1])[0]

        if min_dist_node == dst:
            break

        vertices.remove(min_dist_node)

        for neighbor in weighted_graph.vertices[min_dist_node].adjacent:

            distance = weighted_graph.vertices[min_dist_node].adjacent[neighbor]

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                prev[neighbor] = min_dist_node

    # trace back from dst
    path = []
    current = dst
    while prev[current]:
        path.append(current)
        current = prev[current]
    path.append(current)

    return path[::-1]

