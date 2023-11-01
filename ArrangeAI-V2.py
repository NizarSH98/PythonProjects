import tkinter as tk
import random
from collections import deque
import heapq


'''class Solver:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def solve(self):
        visited = set()
        queue = deque([(self.puzzle.board, self.puzzle.empty_pos, [])])

        while queue:
            current_board, empty_pos, moves = queue.popleft()

            if self.puzzle.is_solved(current_board):
                return moves

            visited.add(tuple(map(tuple, current_board)))

            for move in self.puzzle.moves:
                new_i = empty_pos[0] + move[0]
                new_j = empty_pos[1] + move[1]

                if 0 <= new_i < 3 and 0 <= new_j < 3:
                    new_board = [row[:] for row in current_board]
                    new_board[empty_pos[0]][empty_pos[1]], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[empty_pos[0]][empty_pos[1]]

                    if tuple(map(tuple, new_board)) not in visited:
                        queue.append((new_board, (new_i, new_j), moves + [(new_i, new_j)]))

        return None'''





class FifteenPuzzle:
    def __init__(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.empty_pos = (3, 3)
        self.moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        self.window = tk.Tk()
        self.window.title("15 Puzzle")

        self.buttons = [[tk.Button(self.window, text=str(i*3+j+1), command=lambda i=i, j=j: self.make_move(i, j), width=5, height=2, font=('Helvetica', 16))
                         for j in range(3)] for i in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)

        self.shuffle()
        self.update_zero_color()  

        self.solve_button = tk.Button(self.window, text="Solve", command=self.solve_puzzle)
        self.solve_button.grid(row=3, column=0, columnspan=3, pady=(10, 0))

    def shuffle(self):
        nums = list(range(1, 9))
        nums.append(0)
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                if nums[i*3+j] == 0:
                    self.empty_pos = (i, j)
                self.board[i][j] = nums[i*3+j]
                self.buttons[i][j].config(text=str(nums[i*3+j]))

    def make_move(self, i, j):
        if (i, j) in self.get_valid_moves():
            self.swap(i, j, self.empty_pos[0], self.empty_pos[1])
            self.empty_pos = (i, j)
            self.update_gui()
            self.update_zero_color() 
            self.is_solved()  

    def swap(self, i1, j1, i2, j2):
        self.board[i1][j1], self.board[i2][j2] = self.board[i2][j2], self.board[i1][j1]
        self.buttons[i1][j1].config(text=str(self.board[i1][j1]))
        self.buttons[i2][j2].config(text=str(self.board[i2][j2]))

    def get_valid_moves(self):
        valid_moves = []
        for move in self.moves:
            new_i = self.empty_pos[0] + move[0]
            new_j = self.empty_pos[1] + move[1]
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                valid_moves.append((new_i, new_j))
        return valid_moves

    def update_gui(self):
        self.window.update()

    def update_zero_color(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    self.buttons[i][j].config(bg='lightblue')  
                else:
                    self.buttons[i][j].config(bg='SystemButtonFace')

    def is_solved(self, board):
        flattened_list = [item for sublist in board for item in sublist]
        sorted_list = sorted(flattened_list)
        
        return flattened_list == sorted_list


    def solve_puzzle(self):
        solver = Solver(self)
        moves = solver.solve()
        if moves:
            self.animate_solution(moves)

    def animate_solution(self, moves):
        for move in moves:
            i, j = self.empty_pos
            new_i = i + move[0]
            new_j = j + move[1]
            self.make_move(new_i, new_j)          
     
if __name__ == "__main__":
    puzzle = FifteenPuzzle()
    puzzle.window.protocol("WM_DELETE_WINDOW", puzzle.window.quit)  
    puzzle.window.mainloop()