from flask import Flask, render_template

app = Flask(__name__)

with open("Bot.py") as file:
    exec(file.read())

@app.route("/")
def HomePage():
    return render_template("HomePage.html")

if __name__ == "__main__" :
    app.run(debug=True)