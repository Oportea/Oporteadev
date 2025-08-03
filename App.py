from flask import Flask, redirect, render_template
import os

app = Flask(__name__)

@app.route("/")
def HomePage():
    return render_template("HomePage.html")

if __name__ == "__main__" :
    app.run(debug=True)