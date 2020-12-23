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
        if board is not None:
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

        self.N = len(self.board[0])
        self.numbers = np.arange(1, self.N + 1)

    def solve(self):
        empty_places = self.find_empty()
        if empty_places == []:
            return True

        for i in self.numbers:
            taken = self.check_row_and_cols(empty_places[0])
            usable_numbers = [x for x in self.numbers if x not in taken]
            if i in usable_numbers:
                self.board[empty_places[0][0]][empty_places[0][1]] = i

                if self.solve() is True:
                    return True

                self.board[empty_places[0][0]][empty_places[0][1]] = 0

        return False

    def find_empty(self):
        empty = []
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if col == 0:
                    empty.append([i, j])

        return empty

    def check_row_and_cols(self, pos):
        col = [col[pos[1]] for col in self.board]
        row = self.board[pos[0]]
        no_go = list(set(col + row))
        if 0 in no_go:
            no_go.remove(0)
        return no_go


if __name__ == '__main__':
    solver = Solve_sudoku()
    solver.solve()
    print(solver.board)
