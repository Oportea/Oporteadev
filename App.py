from flask import Flask, render_template, jsonify
import requests
import struct

app = Flask(__name__)

@app.route("/")
def HomePage():
    x = requests.get('https://api.lanyard.rest/v1/users/1359617287690391724')
    
    return f"<h1>{struct.unpack('>d', x.content)[0]}</h1>"

    #return render_template("HomePage.html")

if __name__ == "__main__" :
    app.run(debug=True)