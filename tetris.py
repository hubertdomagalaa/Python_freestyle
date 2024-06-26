

import pygame
import random

pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)


BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * (GRID_WIDTH + 6)
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT


SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]

COLORS = [CYAN, YELLOW, MAGENTA, RED, GREEN, BLUE, ORANGE]


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

class Tetromino:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = random.choice(SHAPES)
        self.color = COLORS[SHAPES.index(self.shape)]
        self.rotation = 0

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)

    def get_shape(self):
        return self.shape[self.rotation]

def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            if (x, y) in locked_positions:
                grid[y][x] = locked_positions[(x, y)]
    return grid

def draw_grid(surface, grid):
    for y, row in enumerate(grid):
        for x, color in enumerate(row):
            pygame.draw.rect(surface, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    
    for x in range(GRID_WIDTH + 1):
        pygame.draw.line(surface, WHITE, (x * BLOCK_SIZE, 0), (x * BLOCK_SIZE, SCREEN_HEIGHT))
    for y in range(GRID_HEIGHT + 1):
        pygame.draw.line(surface, WHITE, (0, y * BLOCK_SIZE), (GRID_WIDTH * BLOCK_SIZE, y * BLOCK_SIZE))

def draw_tetromino(surface, tetromino):
    shape = tetromino.get_shape()
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(surface, tetromino.color,
                                 ((tetromino.x + x) * BLOCK_SIZE, (tetromino.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

def valid_move(tetromino, grid):
    for y, row in enumerate(tetromino.get_shape()):
        for x, cell in enumerate(row):
            if cell:
                if (tetromino.x + x < 0 or tetromino.x + x >= GRID_WIDTH or
                    tetromino.y + y >= GRID_HEIGHT or
                    grid[tetromino.y + y][tetromino.x + x] != BLACK):
                    return False
    return True

def clear_rows(grid, locked):
    full_rows = []
    for y, row in enumerate(grid):
        if BLACK not in row:
            full_rows.append(y)
    
    for row in full_rows:
        del locked[row]
        for y in range(row, 0, -1):
            for x in range(GRID_WIDTH):
                locked[(x, y)] = locked.get((x, y-1), BLACK)
    
    return len(full_rows)

def draw_score(surface, score, high_score):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
    surface.blit(score_text, (GRID_WIDTH * BLOCK_SIZE + 10, 10))
    surface.blit(high_score_text, (GRID_WIDTH * BLOCK_SIZE + 10, 50))

def main():
    clock = pygame.time.Clock()
    grid = create_grid()
    current_piece = Tetromino(GRID_WIDTH // 2 - 1, 0)
    next_piece = Tetromino(GRID_WIDTH // 2 - 1, 0)
    locked_positions = {}
    score = 0
    high_score = 0
    fall_speed = 0.5
    fall_time = 0

    running = True
    while running:
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_move(current_piece, grid):
                current_piece.y -= 1
                for y, row in enumerate(current_piece.get_shape()):
                    for x, cell in enumerate(row):
                        if cell:
                            locked_positions[(current_piece.x + x, current_piece.y + y)] = current_piece.color
                current_piece = next_piece
                next_piece = Tetromino(GRID_WIDTH // 2 - 1, 0)
                score += clear_rows(grid, locked_positions) * 100
                if score > high_score:
                    high_score = score

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_move(current_piece, grid):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_move(current_piece, grid):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_move(current_piece, grid):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotate()
                    if not valid_move(current_piece, grid):
                        current_piece.rotate()
                        current_piece.rotate()
                        current_piece.rotate()

        grid = create_grid(locked_positions)
        screen.fill(BLACK)
        draw_grid(screen, grid)
        draw_tetromino(screen, current_piece)
        draw_score(screen, score, high_score)
        pygame.display.update()

        if not valid_move(current_piece, grid):
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()