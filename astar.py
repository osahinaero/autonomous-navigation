grid = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0]
]

rows = len(grid)
cols = len(grid[0])

start = (0, 0)
target = (4, 2)

moves = [(1,0), (0,1), (0,-1), (-1,0)]

def h(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

open_set = [start]
came_from = {}

g = {start: 0}
f = {start: h(start, target)}

while open_set:
    current = min(open_set, key=lambda pos: f.get(pos, float("inf")))
    print("Current:", current)

    if current == target:
        print("Reached target!")
        break

    open_set.remove(current)

    for dx, dy in moves:
        nx, ny = current[0] + dx, current[1] + dy
        neighbor = (nx, ny)

        if nx < 0 or nx >= cols or ny < 0 or ny >= rows:
            continue

        if grid[ny][nx] == 1:
            continue

        tentative_g = g[current] + 1

        if tentative_g < g.get(neighbor, float("inf")):
            came_from[neighbor] = current
            g[neighbor] = tentative_g
            f[neighbor] = tentative_g + h(neighbor, target)

            if neighbor not in open_set:
                open_set.append(neighbor)
