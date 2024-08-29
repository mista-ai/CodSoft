from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Initialize scores and round counter
user_score = 0.0
computer_score = 0.0
round_counter = 0

# Possible choices
choices = ['rock', 'paper', 'scissors']


def determine_winner(user_choice, computer_choice):
    global user_score, computer_score

    if user_choice == computer_choice:
        user_score += 0.5
        computer_score += 0.5
        return "It's a tie!"

    if (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "You lose!"


@app.route("/", methods=['GET', 'POST'])
def index():
    global round_counter
    if request.method == 'POST':
        if 'choice' in request.form:
            user_choice = request.form['choice']
            computer_choice = random.choice(choices)
            result = determine_winner(user_choice, computer_choice)
            round_counter += 1

            return render_template('index.html', user_choice=user_choice,
                                   computer_choice=computer_choice, result=result,
                                   user_score=user_score, computer_score=computer_score,
                                   round_counter=round_counter)
        elif 'continue' in request.form:
            return redirect(url_for('index'))

    return render_template('index.html', user_score=user_score,
                           computer_score=computer_score, round_counter=round_counter)


@app.route("/reset")
def reset_scores():
    global user_score, computer_score, round_counter
    user_score = 0.0
    computer_score = 0.0
    round_counter = 0
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
