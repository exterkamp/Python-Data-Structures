def depth_first_search(grid, start, target):
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

    stack = [(x_start, y_start)]
    visited.add((x_start, y_start))
    
    while stack:
        current = stack.pop()
        
        for coor in [(current[0], current[1]-1),(current[0]-1, current[1]),(current[0]+1, current[1]),(current[0], current[1]+1)]:
            if coor[0] < 0 or coor[0] > width-1 or coor[1] < 0 or coor[1] > height-1:
                continue
            if grid[coor[1]][coor[0]] == target:
                return coor
            else:
                if coor not in visited:
                    stack.append(coor)
                    visited.add(current)
    return None
