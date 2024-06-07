from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    return "Flask Working fine"
if __name__ == "__main__": 
    app.run()
@app.route("/login")
def template():
    return render_template("index.html")
