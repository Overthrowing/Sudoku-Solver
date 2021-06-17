import PySimpleGUI as sg

from main import *

BOX_SIZE = 47
layout = [
    [sg.Graph((800, 800), (0, 450), (450, 0), key='-GRAPH-',
              change_submits=True, drag_submits=False)],
]

window = sg.Window('Sudoku Solver', layout, finalize=True)
g = window['-GRAPH-']
for row in range(9):
    for col in range(9):
        g.draw_rectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3),
                         (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
        g.draw_text('{}'.format(board[row][col]),
                    (row * BOX_SIZE + 18, col * BOX_SIZE + 17), text_location="center")


def solve(board, t=0):
    if solved(board):
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
        return True
    else:
        row, col = find_empty(board)

    for i in range(1, 10):
        if valid(board, i, row, col):
            board[row][col] = i
            draw(board, row, col, t)
            window.finalize()
            if solve(board, t):
                return True

            board[row][col] = 0
            draw(board, row, col, t)
            window.finalize()

    return False


def draw(board, r, c, t):
    g.erase()
    for row in range(9):
        for col in range(9):
            if (row, col) == (r, c):
                g.draw_rectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3),
                                 (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black',
                                 fill_color=("green"))
                if board[row][col] != 0:
                    g.draw_text('{}'.format(board[row][col]),
                                (col * BOX_SIZE + 10, row * BOX_SIZE + 8), font=("courier", 17),
                                text_location="center")
            elif board[row][col] == 0:
                g.draw_rectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3),
                                 (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
            else:
                g.draw_rectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3),
                             (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')

                g.draw_text('{}'.format(board[row][col]),
                        (col * BOX_SIZE + 10, row * BOX_SIZE + 8), font=("courier", 17), text_location="center")
    time.sleep(t)


if __name__ == '__main__':
    solve(board, 0.3)
