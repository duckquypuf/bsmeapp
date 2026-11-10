from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/player', methods=['POST'])
def player_view():
  player_name = request.form.get('player_name')

  # TODO: use ACTUAL DATA
  activities = [
      {'sport': 'Football', 'wins': 3, 'losses': 1, 'draws': 0, 'points': 9},
      {'sport': 'Swimming', 'wins': 2, 'losses': 0, 'draws': 1, 'points': 7},
  ]

  return render_template(
      'player.html', player_name=player_name, activities=activities
  )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
