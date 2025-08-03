from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def HomePage():
    return render_template("/HomePage/Index.html")

if __name__ == "__main__" :
    app.run(debug=True)