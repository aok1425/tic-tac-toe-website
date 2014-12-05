from flask import Flask, session, redirect, url_for, escape, request, render_template
from game import *

app = Flask(__name__)
board = [None for i in range(9)]

# player is 1, computer is 0

def computer_move():
    count_of_moves = 0
    
    for position, square in enumerate(board):
        if square != None:
            count_of_moves += 1
            last_square = position

    if count_of_moves <= 1:
        if last_square == 8:
            board[0] = 0
        else:
            board[last_square + 1] = 0
    else:
        if check_win(board)[0]:
            print_win(board)

        print '\nNow, computer goes...\n'

        move = move_helper(board, 0)
        print 'this was the move that computer tried:', move[1]
        board[move[1]] = 0

        if check_win(board)[0]:
            print_win(board)

def computer_move():
    if check_win(board)[0]:
        print_win(board)

    print '\nNow, computer goes...\n'

    move = move_helper(board, 0)
    print 'this was the move that computer tried:', move[1]
    board[move[1]] = 0

    if check_win(board)[0]:
        print_win(board)

@app.route('/')
def index():
    return render_template('dashboard.html', board=enumerate(board, 1))

@app.route('/1')
def one():
    board[0] = 1
    computer_move()
    return render_template('dashboard.html', board=enumerate(board, 1))

@app.route('/2')
def two():
    board[1] = 1
    computer_move()
    return render_template('dashboard.html', board=enumerate(board, 1))

@app.route('/3')
def three():
    board[2] = 1
    computer_move()
    return render_template('dashboard.html', board=enumerate(board, 1))

@app.route('/4')
def four():
    board[3] = 1
    computer_move()
    return render_template('dashboard.html', board=enumerate(board, 1))

@app.route('/5')
def five():
    board[4] = 1
    computer_move()
    return render_template('dashboard.html', board=enumerate(board, 1))

@app.route('/6')
def six():
    board[5] = 1
    computer_move()
    return render_template('dashboard.html', board=enumerate(board, 1))

@app.route('/7')
def seven():
    board[6] = 1
    computer_move()
    return render_template('dashboard.html', board=enumerate(board, 1))

@app.route('/8')
def eight():
    board[7] = 1
    computer_move()
    return render_template('dashboard.html', board=enumerate(board, 1))

@app.route('/9')
def nine():
    board[8] = 1
    computer_move()
    return render_template('dashboard.html', board=enumerate(board, 1))

@app.route('/new')
def new():
    for i in range(9):
        board[i] = None
    return render_template('dashboard.html', board=enumerate(board, 1))

# set the secret key.  keep this really secret:
app.secret_key = 'alex'

if __name__ == '__main__':
    app.run(debug=True)