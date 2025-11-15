from flask import Flask

app = Flask(__name__)

@app.route("/")
def heloo_word():
    return "michel e viado"
@app.route("/about")
def about():
    return "pagina sobre"

if __name__ == "__main__":
    app.run(debug=True)

