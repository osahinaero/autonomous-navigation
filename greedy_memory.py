grid = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0]
]

rows = len(grid)
cols = len(grid[0])

x, y = 0, 0
target = (4, 2)

moves = [(1,0), (0,1), (0,-1), (-1,0)]

visited = set()

for step in range(30):
    print("\nCurrent:", (x, y))

    if (x, y) == target:
        print("Reached target!")
        break

    visited.add((x, y))

    best_move = None
    best_distance = float("inf")

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= cols or ny < 0 or ny >= rows:
            continue

        if grid[ny][nx] == 1:
            continue

        if (nx, ny) in visited:
            continue

        dist = abs(target[0] - nx) + abs(target[1] - ny)

        if dist < best_distance:
            best_distance = dist
            best_move = (nx, ny)

    if best_move is None:
        print("No moves left")
        break

    x, y = best_move
    print("Moved to:", (x, y))
