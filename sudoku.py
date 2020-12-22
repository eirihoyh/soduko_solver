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
        if board == None:
            self.board = board
        else:
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


if __name__ == '__main__':
    solver = Solve_sudoku()
