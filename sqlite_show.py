rom flask import Flask, render_template
import sqlite3
app = Flask(_name_)
@app.route('/')
def show_data():
    conn = sqlite3.connect('your_database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM your_table')
    data = c.fetchall()
    conn.close()
    return render_template('show_data.html', data=data)
if _name_ == '_main_':
    app.run(debug=True)