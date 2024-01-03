from flask import Flask, render_template, request

app = Flask(__name__)

tasks = []  # In-memory task list

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    name = request.form['name']
    task = request.form['task']
    completed = request.form.get('completed', False)  # Default to uncompleted
    tasks.append({'name': name, 'task': task, 'completed': completed})
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
