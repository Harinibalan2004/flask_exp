app = Flask(_name_)
conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT)''')
conn.commit()
conn.close()
@app.route('/add_task', methods=['POST'])
def add_task():
    if request.method == 'POST':
        task = request.json.get('task')
        if task:
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
            conn.commit()
            conn.close()
            return jsonify({'message': 'Task added successfully'}), 200
        else:
            return jsonify({'error': 'No task provided'}), 400
if _name_ == '_main_':
    app.run(debug=True)