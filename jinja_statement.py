from flask import Flask
app = Flask(_name_)
from app import routes
from flask import render_template
from app import app
@app.route("/")
def index():
    items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    return render_template('items.html', items=items)