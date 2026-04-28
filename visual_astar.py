import pygame
import time

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

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# PYGAME SETUP
pygame.init()
cell_size = 100
width = cols * cell_size
height = rows * cell_size

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Autonomous Navigation")

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

def draw_grid(current, path=set()):
    screen.fill(WHITE)

    for y in range(rows):
        for x in range(cols):
            rect = pygame.Rect(x*cell_size, y*cell_size, cell_size, cell_size)

            if grid[y][x] == 1:
                pygame.draw.rect(screen, BLACK, rect)
            elif (x,y) == current:
                pygame.draw.rect(screen, BLUE, rect)
            elif (x,y) == target:
                pygame.draw.rect(screen, RED, rect)
            elif (x,y) in path:
                pygame.draw.rect(screen, GREEN, rect)
            else:
                pygame.draw.rect(screen, (200,200,200), rect, 1)

    pygame.display.update()

# A* setup
open_set = [start]
came_from = {}

g_score = {start: 0}
f_score = {start: heuristic(start, target)}

running = True

while open_set and running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current = min(open_set, key=lambda pos: f_score.get(pos, float("inf")))

    draw_grid(current, came_from.keys())
    time.sleep(0.4)

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

        tentative_g = g_score[current] + 1

        if tentative_g < g_score.get(neighbor, float("inf")):
            came_from[neighbor] = current
            g_score[neighbor] = tentative_g
            f_score[neighbor] = tentative_g + heuristic(neighbor, target)

            if neighbor not in open_set:
                open_set.append(neighbor)

pygame.quit()