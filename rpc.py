from flask import Flask, render_template_string
import random

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Choose one</h1>
    <p><a href='/r'>Rock</a></p>
    <p><a href='/p'>Paper</a></p>
    <p><a href='/s'>Scissors</a></p>
    """

@app.route('/<guess>')
def get_data(guess):
    comp = random.choice(["s", "r", "p"])
    result = ""

    if guess == comp:
        result = "It's a tie!"
    elif (guess == "s" and comp == "p") or (guess == "p" and comp == "r") or (guess == "r" and comp == "s"):
        result = "You won!"
    else:
        result = "Better luck next time"
        
    return render_template_string('''
        <h1>{{ result }}</h1>
        <p>You chose: {{ guess }}</p>
        <p>Computer chose: {{ comp }}</p>
        <p><a href='/'>Play again</a></p>
        {% if result == "Better luck next time" %}
            <img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDlya3Vzd2NnYWdpN2JmNnhxcHExempqbzl3MDgzYmt6NXRvem51byZlcD12MV9pbnRlcm5fbmF0aXZlJmN0PWc/jnQYWZ0T4mkhCmkzcn/giphy.webp'>
        {% endif %}
    ''', result=result, guess=guess, comp=comp)

if __name__ == "__main__":
    app.run(debug=True)

