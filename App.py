from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def HomePage():
    Request = requests.get('https://api.lanyard.rest/v1/users/1359617287690391724')
    Content = Request.content.replace("b", '', 1)
    Content = Content.replace("'", '')
    return f"<h1>{Content}</h1>"

    #return render_template("HomePage.html")

if __name__ == "__main__" :
    app.run(debug=True)