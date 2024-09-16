from flask import Flask, render_template, request, redirect, url_for

from game_condition_checker import GameCondition
from game_logic import GameLogic

# Keep the overall functionality of the program here

app = Flask(__name__,
            template_folder='../templates',
            static_folder='../static')
game = GameLogic()
game_condition = GameCondition(game.board, game.empty)

@app.route('/')
def index():
    winner = game_condition.check_win()
    draw = game_condition.check_draw()
    return render_template('index.html', board=game.board, current_player=game.current_player, winner=winner, draw=draw)

@app.route('/play/<int:cell>')
def play(cell):
    game.play_turn(cell)
    return redirect(url_for('index'))


@app.route('/reset')
def reset():
    game.__init__()
    game_condition.__init__(game.board, game.empty)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)