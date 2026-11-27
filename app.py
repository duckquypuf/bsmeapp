from flask import Flask, render_template, request #type: ignore

schools = [
    {'name': 'St. Christophers School', 'points': 20, 'position': 1},
    {'name': 'British School Bahrain', 'points': 17, 'position': 2},
    {'name': 'Bahrain Bayan School', 'points': 15, 'position': 3},
    {'name': 'Ibn Khuldoon National School', 'points': 14, 'position': 4},
    {'name': 'Riffa Views International School', 'points': 11, 'position': 5},
    {'name': 'Nadeen School', 'points': 9, 'position': 6},
    {'name': 'Abdulrahman Kanoo International School', 'points': 6, 'position': 7},
]

football = [
    {'school': 'St. Christophers School', 'gf': 19, 'ga': 8, 'wins': 6, 'draws': 2, 'losses': 1, 'points': 20, 'position': 1},
    {'school': 'British School Bahrain', 'gf': 18, 'ga': 7, 'wins': 5, 'draws': 2, 'losses': 1, 'points': 17, 'position': 2},
    {'school': 'Bahrain Bayan School', 'gf': 13, 'ga': 11, 'wins': 4, 'draws': 1, 'losses': 3, 'points': 13, 'position': 3},
    {'school': 'Ibn Khuldoon National School', 'gf': 11, 'ga': 12, 'wins': 3, 'draws': 2, 'losses': 3, 'points': 11, 'position': 4},
    {'school': 'Riffa Views International School', 'gf': 9, 'ga': 13, 'wins': 2, 'draws': 2, 'losses': 4, 'points': 8, 'position': 5},
    {'school': 'Nadeen School', 'gf': 7, 'ga': 15, 'wins': 1, 'draws': 3, 'losses': 4, 'points': 6, 'position': 6},
    {'school': 'Abdulrahman Kanoo International School', 'gf': 5, 'ga': 18, 'wins': 1, 'draws': 1, 'losses': 6, 'points': 4, 'position': 7},
]

# School: list of players
# structure can be changed
players = [
   {
      'school':'St. Christophers School',
      'name':'someone',
      'sports':[
            {'sport':'football','goals':2},
      ],
   },
]

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html', schools=schools, football_standings=football)

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

