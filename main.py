import time

board = [[2, 5, 0, 0, 1, 0, 0, 0, 9],
         [0, 7, 1, 0, 0, 0, 0, 8, 0],
         [0, 0, 3, 6, 0, 4, 0, 0, 0],
         [7, 0, 9, 5, 0, 0, 0, 0, 4],
         [0, 4, 0, 0, 0, 9, 0, 0, 0],
         [0, 0, 0, 4, 0, 7, 0, 0, 8],
         [0, 1, 8, 0, 5, 0, 9, 0, 0],
         [9, 0, 0, 1, 0, 0, 5, 0, 7],
         [0, 2, 0, 0, 4, 0, 8, 6, 1]]


def render(board):
    def expand_line(line):
        return line[0] + line[5:9].join([line[1:5] * (3 - 1)] * 3) + line[9:13]

    line0 = expand_line("╔═══╤═══╦═══╗")
    line1 = expand_line("║ . │ . ║ . ║")
    line2 = expand_line("╟───┼───╫───╢")
    line3 = expand_line("╠═══╪═══╬═══╣")
    line4 = expand_line("╚═══╧═══╩═══╝")

    symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = [[""] + [symbol[n] for n in row] for row in board]
    print(line0)
    for r in range(1, 9 + 1):
        print("".join(n + s for n, s in zip(nums[r - 1], line1.split("."))))
        print([line2, line3, line4][(r % 9 == 0) + (r % 3 == 0)])


# Utility functions
def find_empty(board):
    for row in range(9):
        for item in range(9):
            if board[row][item] == 0:
                return [row, item]


def get_column(board, c):
    return [row[c] for row in board]


def get_group(board, r, c):
    group_y = r // 3
    group_x = c // 3
    group = []
    for row in range(group_y * 3, group_y * 3 + 3):
        for item in range(group_x * 3, group_x * 3 + 3):
            group.append(board[row][item])
    return (group)


# Solving functions
def valid(bo, num, r, c):
    # Check row
    for i in range(len(bo[0])):
        if bo[r][i] == num and c != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][c] == num and r != i:
            return False

    # Check box
    box_x = c // 3
    box_y = r // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != (r, c):
                return False

    return True


def solved(board):
    for row in range(9):
        for column in range(9):
            if valid(board, board[row][column], row, column) is False or not board[row][column]:
                return False

    return True


def solve(board, render=False, t=0):
    if solved(board):
        return True
    else:
        row, col = find_empty(board)

    for i in range(1, 10):
        if valid(board, i, row, col):
            board[row][col] = i
            if render:
                render(board)
                time.sleep(t)
            if solve(board):
                return True

            board[row][col] = 0
            if render:
                render(board)
                time.sleep(t)

    return False


if __name__ == '__main__':
    print("Original:")
    render(board)
    print("Solved:")
    solve(board)
