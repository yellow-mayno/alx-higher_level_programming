#!/usr/bin/python3
def pascal_triangle(n):
    """ fdsgsfdg sdf gdsf gsfd g

    Args:
        n: filename

    Returns:
        list: dfsgdf dfg dfs dfg

    """

    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [[1], [1, 1]]
    else:
        current = []
        new = pascal_triangle(n - 1).copy()
        previous = new[-1]
        current.append(1)
        i = 0
        for i in range(len(previous) - 1):
            current.append(previous[i] + previous[i + 1])
        current.append(1)
        new.append(current)
        return new
    
