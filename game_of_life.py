import time
import os

class Game_of_life :
    def __init__(self, size=30, population = 0.1):
        self.size = size
        self.board = [[0 for x in range(int(size*1.5))] for y in range(size)]
        import random
        for i in range(size):
            for j in range(size):
                if random.random() < population:
                    self.board[i][j] = 1
                else:
                    self.board[i][j] = 0


    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 1:
                    print(f"\033[47m{' '}\033[0m", end='')
                else:
                    print(' ', end='')
            print()

    def next_generation(self):
        new_board = [[0 for x in range(self.size)] for y in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                count = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x == 0 and y == 0:
                            continue
                        if i + x < 0 or i + x >= self.size or j + y < 0 or j + y >= self.size:
                            continue
                        count += self.board[i + x][j + y]
                if count == 3 or (count == 2 and self.board[i][j] == 1):
                    new_board[i][j] = 1
        self.board = new_board
    def run(self, n=50):
        for i in range(n):
            self.print_board()
            self.next_generation()
            print()
            time.sleep(0.5)
            os.system('cls')