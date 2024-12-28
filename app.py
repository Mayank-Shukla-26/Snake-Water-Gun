from flask import Flask, render_template, request
import random

app = Flask(__name__)

scores = {"user": 0, "computer": 0}

def snake_water_gun_logic(youstr):
    '''
    1 for snake
    -1 for water
    0 for gun
    '''
    computer = random.choice([-1, 0, 1])
    youDict = {"s": 1, "w": -1, "g": 0}
    reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
    you = youDict[youstr]

    result = f"You chose {reverseDict[you]}<br>Computer chose {reverseDict[computer]}<br>"

    if computer == you:
        result += "It's a draw!"
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        result += "You win!"
        scores["user"] += 1
    else:
        result += "You lose!"
        scores["computer"] += 1
    return result

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    youstr = request.form['choice']
    result = snake_water_gun_logic(youstr)
    return render_template('index.html', result=result, user_score=scores['user'], computer_score=scores['computer'])

if __name__ == "__main__":
    app.run(debug=True)
