from flask import Flask # type: ignore
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)
comp =""
clicked = 0

@app.route('/')
def home():
    return "<h1>Choose one</h1>" \
           "<p>r for Rock</p>"\
           "<p>p for paper</p>"\
           "<p>s for scissors</p>"
           


@app.route("/<guess>")
def get_Data(guess):
    
    comp = random.choice(["s", "r", "p"])
    clicked += 1
    print(comp)
    print(clicked)
    if guess == "s" and comp == "p":
        return "<h1>You won</h1>"
    elif guess == "p" and comp == "r":
        return "<h1>You won</h1>"
    elif guess == "r" and comp == "s":
        return "<h1>You won</h1>"
    else:
        return "<h1>Better luck next time</h1> <br>"\
               "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDlya3Vzd2NnYWdpN2JmNnhxcHExempqbzl3MDgzYmt6NXRvem51byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jnQYWZ0T4mkhCmkzcn/giphy.webp'>"

if __name__ == "__main__":
    app.run(debug=True)