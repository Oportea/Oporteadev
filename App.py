from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def HomePage():
    x = requests.get('https://w3schools.com')
    return f"<h1>{x.status_code}</h1>"

    #return render_template("HomePage.html")

if __name__ == "__main__" :
    app.run(debug=True)