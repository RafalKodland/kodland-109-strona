from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Witaj świecie!</h1> <a href='/liczba'>Przejdź do strony z losową liczbą</a>"

@app.route("/liczba")
def losowa_liczba():
    return f"<p>Losowa liczba: {randint(1, 100)}</p> <a href='/'>Przejdź do strony głównej</a>"

app.run(debug=True)