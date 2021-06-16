from main import *
import PySimpleGUI as sg
import time

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

def solve(board):
    if solved(board):
        while True:
            time.sleep(10)
        return True
    else:
        row, col = find_empty(board)

    for i in range(1, 10):
        if valid(board, i, row, col):
            board[row][col] = i
            draw(board, row, col)
            window.finalize()
            if solve(board):
                return True

            board[row][col] = 0
            draw(board, row, col)
            window.finalize()

    return False

def draw(board, r, c):
    g.erase()
    for row in range(9):
        for col in range(9):
            if (row, col) == (r, c):
                g.draw_rectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3),
                                 (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black', fill_color=("green"))
                g.draw_text('{}'.format(board[row][col]),
                            (col * BOX_SIZE + 10, row * BOX_SIZE + 8), color='red', font=("courier", 17), text_location="center")

            g.draw_rectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3),
                             (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')

            g.draw_text('{}'.format(board[row][col]),
                        (col * BOX_SIZE + 10, row * BOX_SIZE + 8), font=("courier", 17), text_location="center")
    time.sleep(0.3)

solve(board)