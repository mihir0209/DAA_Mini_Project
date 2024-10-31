def solve_n_queens_step_by_step(n, callback):
    board = [-1] * n

    def is_safe(row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def place_queen(row):
        if row == n:
            callback(board[:])
            return True
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                callback(board[:])
                if place_queen(row + 1):
                    return True
                board[row] = -1
                callback(board[:])
        return False

    place_queen(0)
