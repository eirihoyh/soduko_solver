import numpy as np

class Solve_sudoku:
    board = [[3, 5, 0, 9, 0, 6, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 9, 0],
             [0, 0, 6, 0, 0, 6, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [2, 0, 0, 0, 7, 0, 0, 0, 8],
             [8, 9, 0, 0, 0, 5, 1, 0, 4],
             [6, 3, 0, 0, 4, 0, 0, 5, 7],
             [0, 0, 0, 0, 9, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 3, 0, 0]]

    def __init__(self, board=None):

        if board != None:
            row_length = len(board[0])
            i = 0
            for row in board:
                if len(row) != row_length:
                    raise RuntimeError("Board must have equal row length")
                i += 1

            if i == row_length:
                self.board = board
                print(board)
            else:
                raise RuntimeError("Board must be quadratic")

        self.numbers = np.arange(1,10)
        self.positions = []

    def solve(self, pos, used_numbers=0):
        if used_numbers == 0:
            used_numbers = [0]

        usable_numbers = [x for x in self.numbers if x not in used_numbers]
        for number in usable_numbers:
            if number != 0:
                self.board[pos[0]][pos[1]] = number
            for i, row in enumerate(
                    self.board):  # This mus be something else than self.board or something
                for j, col in enumerate(row):
                    if number == 0:
                        used_numbers = self.check_row_and_cols([i, j])
                        self.solve([i, j], used_numbers)

    def check_row_and_cols(self, pos):
        row = [row[pos[0]] for row in self.board]
        col = self.board[pos[1]]
        return list(set(col+row))



if __name__ == '__main__':
    solver = Solve_sudoku()
    print(solver.numbers)
