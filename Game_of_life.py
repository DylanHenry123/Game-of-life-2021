# Making Conoway's game of life
# This is the working version of the game of life

# 1 stands for a cell being alive
# 0 stands for a cell being dead
# Neighbours can be diagonal or adjacent. They are the 8 cells surrounding the cell.

# Rules
# Any live cell with fewer than two neighbours dies, as if caused by underpopulation
# Any live cell with two or three live neighbours lives on to the next generation
# Any live cell with more than three neighbours dies, as if overpopulation
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction

import random
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FPS = 60

WIDTH = HEIGHT = 900
ROWS = COLS = 30
SQ_SIZE = WIDTH // ROWS

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


class Game:
    """
    This is the version that works
    """
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[random.randint(0, 1) for _ in range(self.rows)] for _ in range(self.cols)]
        self.next = [[0 for _ in range(ROWS)] for _ in range(COLS)]

    def draw_grid(self, screen):
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == 1:
                    pygame.draw.rect(screen, BLACK, pygame.Rect(r * SQ_SIZE, c * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    pygame.display.update()
                if self.grid[r][c] == 0:
                    pygame.draw.rect(screen, WHITE, pygame.Rect(r * SQ_SIZE, c * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    pygame.display.update()

    def count_neighbours(self, r, c):
        summation = 0
        if r == 0 and not(c == 0 or c == self.cols - 1):
            for i in range(0, 2, 1):
                for j in range(-1, 2, 1):
                    summation += self.grid[r + i][c + j]

                summation -= self.grid[r][c]

        elif r == self.rows - 1 and not(c == 0 or c == self.cols - 1):
            for i in range(-1, 1, 1):
                for j in range(-1, 2, 1):
                    summation += self.grid[r + i][c + j]

                summation -= self.grid[r][c]

        elif c == 0 and not(r == 0 or r == self.rows - 1):
            for i in range(-1, 2, 1):
                for j in range(0, 2, 1):
                    summation += self.grid[r + i][c + j]

                summation -= self.grid[r][c]

        elif c == self.rows - 1 and not(r == 0 or r == self.rows - 1):
            for i in range(-1, 2, 1):
                for j in range(-1, 1, 1):
                    summation += self.grid[r + i][c + j]

                summation -= self.grid[r][c]

        elif r == 0 and c == 0:
            for i in range(0, 2, 1):
                for j in range(0, 2, 1):
                    summation += self.grid[r + i][c + j]

                summation -= self.grid[r][c]

        elif r == 0 and c == self.cols - 1:
            for i in range(0, 2, 1):
                for j in range(-1, 1, 1):
                    summation += self.grid[r + i][c + j]

                summation -= self.grid[r][c]

        elif r == self.rows - 1 and c == 0:
            for i in range(-1, 1, 1):
                for j in range(0, 2, 1):
                    summation += self.grid[r + i][c + j]

                summation -= self.grid[r][c]

        elif r == self.rows - 1 and c == self.cols - 1:
            for i in range(-1, 1, 1):
                for j in range(-1, 1, 1):
                    summation += self.grid[r + i][c + j]

                summation -= self.grid[r][c]

        else:
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    summation += self.grid[r + i][c + j]

            summation -= self.grid[r][c]

        return summation


    def next_generation(self):
        for r in range(len(self.grid)):
            for c in range(len(self.grid)):
                summation = self.count_neighbours(r, c)

                if self.grid[r][c] == 1 and summation < 2:
                    self.next[r][c] = 0

                if self.grid[r][c] == 1 and (summation == 2 or summation == 3):
                    self.next[r][c] = 1

                if self.grid[r][c] == 1 and summation > 3:
                    self.next[r][c] = 0

                if self.grid[r][c] == 0 and summation == 3:
                    self.next[r][c] = 1

        self.grid = self.next

    def reset_next(self):
        self.next = [[0 for _ in range(self.rows)] for _ in range(self.cols)]

    def formatted_grid(self):
        for i in range(len(self.grid)):
            print(self.grid[i])


def main():
    run = True
    clock = pygame.time.Clock()

    g = Game(ROWS, COLS)
    g.draw_grid(SCREEN)

    while run:
        clock.tick(FPS)

        g.next_generation()
        g.draw_grid(SCREEN)
        if g.grid == [[0 for _ in range(ROWS)] for _ in range(COLS)]:
            run = False

        g.reset_next()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


if __name__ == '__main__':
    pygame.init()
    main()