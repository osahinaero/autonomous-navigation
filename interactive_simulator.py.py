import pygame
import time

# ===== USER INPUT =====
size = int(input("Enter grid size (e.g. 5, 10, 15): "))

rows = size
cols = size

grid = [[0 for _ in range(cols)] for _ in range(rows)]

cell_size = 60
width = cols * cell_size
height = rows * cell_size + 80  # extra space for button

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Navigation Simulator")

font = pygame.font.SysFont(None, 36)

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
GRAY = (200,200,200)

moves = [(1,0), (0,1), (0,-1), (-1,0)]

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def draw_grid(current, target, path, build_mode):
    screen.fill(WHITE)

    # draw grid
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
                pygame.draw.rect(screen, GRAY, rect, 1)

    # draw button
    button_rect = pygame.Rect(width//2 - 80, rows*cell_size + 20, 160, 40)
    pygame.draw.rect(screen, (100,200,100), button_rect)
    text = font.render("START", True, BLACK)
    screen.blit(text, (button_rect.x + 40, button_rect.y + 5))

    pygame.display.update()
    return button_rect

def astar(start, target):
    open_set = [start]
    came_from = {}

    g = {start: 0}
    f = {start: heuristic(start, target)}

    while open_set:
        current = min(open_set, key=lambda pos: f.get(pos, float("inf")))

        if current == target:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

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
                f[neighbor] = tentative_g + heuristic(neighbor, target)

                if neighbor not in open_set:
                    open_set.append(neighbor)

    return []

# ===== INITIAL STATE =====
current = (0,0)
target = (cols-1, rows-1)
path = []
build_mode = True

running = True

while running:
    button_rect = draw_grid(current, target, path, build_mode)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            # click inside grid
            if my < rows * cell_size:
                gx = mx // cell_size
                gy = my // cell_size

                if build_mode:
                    # LEFT CLICK = add/remove obstacle
                    if event.button == 1:
                        if (gx, gy) != current:
                            grid[gy][gx] = 0 if grid[gy][gx] == 1 else 1

                    # RIGHT CLICK = set target
                    if event.button == 3:
                        if grid[gy][gx] == 0:
                            target = (gx, gy)

            # click START button
            if button_rect.collidepoint(mx, my):
                build_mode = False
                path = astar(current, target)

    # movement phase
    if not build_mode and path:
        current = path.pop(0)
        time.sleep(0.1)

pygame.quit()