from app import app
app = Flask(_name_)
app.config['SECRET_KEY'] = 'your_secret_key'
from app import routes
from flask import render_template, flash, redirect, url_for
from app import app
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            flash(f'Hello, {name}!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Please enter your name.', 'danger')
    return render_template('form.html')
 if _name_ == "_main_":
    app.run(debug=True) 