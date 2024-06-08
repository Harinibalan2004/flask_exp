from flask import Flask, render_template, redirect
import determine
app = Flask(__name__)
@app.route("/frontpage")
def frontpage  
    return render_template("frontpage.html")
@app.route("/resultpage")
def resultpage():
    return render_template("resultpage.html")
@app.route("/printtime")
def printtime():
    current_time = datetime.datetime.now()
    print(f"current DateTime: {current_time}")
    return redirect("/resultpage")
if __name__ == "__main__": 
    app.run(debug=True)
