from collections import deque

def breadth_first_search(grid, start, target):
    """
    Search a 2d grid for a given target starting at start.

    Args:
        grid: the input grid as a List[List]
        start: the start grid in format (x,y) zero index
        target: the target value to find in the grid
    Returns:
        Coordinate of the target. Or None if cannot be found. 
    """
    height = len(grid)
    if not height:
        return None
    width = len(grid[0])

    x_start = start[0]
    y_start = start[1]

    # short circuit the start lookup
    if grid[y_start][x_start] == target:
        return (x_start, y_start)

    visited = set()

    queue = deque([(x_start, y_start)])
    visited.add((x_start, y_start))
    
    while queue:
        current = queue.pop()
        

        for coor in [(current[0], current[1]-1),(current[0]-1, current[1]),(current[0]+1, current[1]),(current[0], current[1]+1)]:
            if coor[0] < 0 or coor[0] > width-1 or coor[1] < 0 or coor[1] > height-1:
                continue
            if grid[coor[1]][coor[0]] == target:
                return coor
            else:
                if coor not in visited:
                    queue.appendleft(coor)
                    visited.add(current)
    return None

def breadth_first_search_graph(head, target):
    """
    Search a graph for a target value.

    Args:
        head: pointer to node in the graph
        targer: the target value to find
    
    Returns:
        Node which has value = target.
    """
    visited = set([head])
    queue = [head]
    
    while queue:
        current = queue.pop()

        for adjacent in current.adjacent_list:
            if adjacent in visited:
                continue
            
            if adjacent.val == target:
                return adjacent
            else:
                queue.insert(0, adjacent)
                visited.add(adjacent)
    return None

