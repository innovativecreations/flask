from flask import Flask, render_template_string # type: ignore
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Choose one</h1>" \
           "<p>r for Rock</p>"\
           "<p>p for paper</p>"\
           "<p>s for scissors</p>"
           


@app.route("/<guess>")
def get_Data(guess):

    comp = random.choice(["s", "r", "p"])
    result =""
    if guess == "s" and comp == "p":
        return render_template_string('''<h1>You won</h1> 
        <p>you chose: {{ guess }}</p>
         <p>comp chose: {{ comp }}</p>''')
    elif guess == "p" and comp == "r":
        return render_template_string('''<h1>You won</h1> 
        <p>you chose: {{ guess }}</p>
         <p>comp chose: {{ comp }}</p>''')
    elif guess == "r" and comp == "s":
        return render_template_string('''<h1>You won</h1> 
        <p>you chose: {{ guess }}</p>
         <p>comp chose: {{ comp }}</p>''')
    elif guess == comp:
        return "TIE"
    else:
        return render_template_string("""<h1>Better luck next time</h1> <p>you chose: {{guess}}</p> <p>comp chose: {comp}</p> <br>
               "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDlya3Vzd2NnYWdpN2JmNnhxcHExempqbzl3MDgzYmt6NXRvem51byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jnQYWZ0T4mkhCmkzcn/giphy.webp'>""")

if __name__ == "__main__":
    app.run(debug=True)