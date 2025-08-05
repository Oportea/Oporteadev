from flask import Flask, render_template
import numpy as np
import requests
import codecs
import json

app = Flask(__name__)

@app.route("/")
def HomePage():
    Request = requests.get('https://api.lanyard.rest/v1/users/1359617287690391724')
    Content = codecs.decode(Request.content)
    return json.loads(Content)["data"]["discord_status"]

    #return render_template("HomePage.html")

if __name__ == "__main__" :
    app.run(debug=True)