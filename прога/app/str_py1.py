from flask import Flask, render_template
app = Flask(__name__)

menu =[{
    "name": "книги", "url": "buy"}
]

@app.route("/")
def index():
    return render_template("str1.html", menu = menu)
@app.route("/book")
def book():
    # return render_template(


if __name__ == "__main__":
    app.run(debug=True)