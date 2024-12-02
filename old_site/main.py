from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route("/")
def hello():
    r = randint(1, 100)
    return render_template("index.html", liczba=r)

@app.route("/liczba")
def losowa_liczba():
    return f"<p>Losowa liczba: {randint(1, 100)}</p> <a href='/'>Przejdź do strony głównej</a>"


@app.route("/<zmienna>")
def test(zmienna):
    return f"<p>{zmienna}</p>"


app.run(debug=True)