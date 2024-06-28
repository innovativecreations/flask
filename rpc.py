from flask import Flask, render_template_string  # type: ignore
import random

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Choose one</h1>
    <p>r for Rock</p>
    <p>p for Paper</p>
    <p>s for Scissors</p>
    """

@app.route('/<guess>')
def get_data(guess):
    comp = random.choice(["s", "r", "p"])
    result = ""
    print(comp)
    if guess == comp:
        result = "It's a tie!"
    elif (guess == "s" and comp == "p") or (guess == "p" and comp == "r") or (guess == "r" and comp == "s"):
        result = "You won!"
    else:
        result = "Better luck next time"

    return render_template_string('''
        <h1>{{ result }}</h1>''',
         result=result)

if __name__ == "__main__":
    app.run(debug=True)
