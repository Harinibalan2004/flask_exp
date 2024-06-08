from flask import Flask, render_template
app = Flask(_name_)
@app.route('/dashboard')
def dashboard():
    name = "Harini
    notification = 4
    mail = 3
    return render_template('dashboard.html', name_temp=name, notification_temp=notification, mail_temp=mail)
if _name_ == '_main_':
    app.run(debug=True)
