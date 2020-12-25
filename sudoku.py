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
        """
        :param board:
            Sudoku board that contains zero
        """
        if board is not None:
            row_length = len(board[0])
            i = 0
            for row in board:
                if len(row) != row_length:
                    raise RuntimeError("Board must have equal row length")
                i += 1

            if i == row_length:
                self.board = board
            else:
                raise RuntimeError("Board must be quadratic")

        self.N = len(self.board[0])
        self.numbers = np.arange(1, self.N + 1)

    def try_to_solve(self):
        """
        Solves sudoku by using backtracking.
        :return:
            Bool, True when done solving and False if not solvable.
        """
        empty_places = self.find_empty()
        if empty_places == True:
            return True

        for i in self.numbers:
            taken = self.taken_numbers(empty_places)
            usable_numbers = [x for x in self.numbers if x not in taken]
            if i in usable_numbers:
                self.board[empty_places[0]][empty_places[1]] = i

                if self.try_to_solve() is True:
                    return True

                self.board[empty_places[0]][empty_places[1]] = 0

        return False

    def find_empty(self):
        """
        find_empty finds the places that contains zero
        :return:
        a list of positions in the board that contains zero
        """
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if col == 0:
                    return [i, j]

        return True

    def taken_numbers(self, pos):
        """
        Find all number in the same row and same column that is already taken
        :param pos:
            Position on the board
        :return:
            A list with all numbers that is not usable for the position.
        """
        col = [col[pos[1]] for col in self.board]
        row = self.board[pos[0]]

        square_row = (int(np.ceil((1 + pos[0]) / 3))) * 3
        square_col = (int(np.ceil((1 + pos[1]) / 3))) * 3
        three_rows = self.board[square_row - 3:square_row]
        square = []
        for diff_rows in three_rows:
            for i in range(square_col - 3, square_col):
                square.append(diff_rows[i])

        no_go = list(set(col + row + square))
        return no_go

    def solve(self):
        if not self.try_to_solve():
            print("This board is not solvable")
        for row in self.board:
            print(f"{row}")


if __name__ == '__main__':
    expert_sudoku = [[0, 0, 0, 7, 0, 0, 0, 0, 0],
                     [8, 0, 5, 9, 0, 4, 3, 0, 0],
                     [0, 6, 4, 0, 0, 0, 9, 1, 0],
                     [0, 0, 0, 0, 0, 5, 0, 2, 0],
                     [0, 0, 0, 0, 0, 0, 1, 8, 0],
                     [0, 0, 0, 0, 0, 2, 0, 0, 6],
                     [0, 0, 9, 6, 0, 1, 2, 0, 0],
                     [2, 8, 0, 0, 0, 0, 7, 0, 0],
                     [0, 0, 1, 4, 0, 7, 0, 0, 0]]

    solver = Solve_sudoku()
    solver.solve()
