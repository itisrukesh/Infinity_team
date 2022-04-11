
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return "<h1>form code</h1>"


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        usr = request.form['uname1']
        email = request.form['email']
        l = [usr , email]
        return render_template("display.html", h=l)
    else:
        return render_template("register.html")


@app.route("/<usr>")
def user(usr, eml):
    return f"<h1>{usr} and {eml} </h1>"


if __name__ == "__main__":
    app.run(debug=True)