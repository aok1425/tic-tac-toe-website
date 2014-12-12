from flask import Flask, session, redirect, url_for, escape, request, render_template
from python.game import *
# from python.original.game import move_helper # for non-memoized version that has non-state/dict Minimax w/choose-first and alpha-beta pruning

app = Flask(__name__)
board = [None for i in range(9)]

# player is 1, computer is 0

def computer_move():
    if check_win(board)[0]:
        return check_win(board) # i could have assigned this to a var, but i think this is more readable, and it's quick anyways.

    print '\nNow, computer goes...\n'

    move = move_helper(board, memoization=True)
    print 'this was the move that computer tried:', move[1]
    board[move[1]] = 0

    if check_win(board)[0]:
        return check_win(board)

# def computer_move(): # this is to have the computer think through the first move
#     if check_win(board)[0]:
#         return check_win(board)

#     print '\nNow, computer goes...\n'

#     move = move_helper(board, memoization=True)
#     print 'this was the move that computer tried:', move[1]
#     board[move[1]] = 0

#     if check_win(board)[0]:
#         return check_win(board)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass # If I could get the CSS right, POST the square value here, and update the board, instead of having a separate URL.
    for i in range(9):
        board[i] = None
    return render_template('index.html', board=enumerate(board, 1), win=[False])

@app.route('/<int:square>')
def mark_square(square):
    board[square - 1] = 1
    win = computer_move()
    return render_template('index.html', board=enumerate(board, 1), win=win)

# set the secret key.  keep this really secret:
app.secret_key = 'alex'

if __name__ == '__main__':
    app.run(debug=True)