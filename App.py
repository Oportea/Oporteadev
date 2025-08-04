from flask import Flask, render_template
import requests

app = Flask(__name__)

with open("Bot.py") as file:
    exec(file.read())

@app.route("/")
def HomePage():
    x = requests.get('https://w3schools.com')
    print(x.status_code)

    #return render_template("HomePage.html")

if __name__ == "__main__" :
    app.run(debug=True)