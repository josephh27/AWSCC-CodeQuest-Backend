# Tested using POSTMAN
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
tasks = []

# Route to get all tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks}), 200

@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if 'title' in data:
        task = {'title': data['title']}
        tasks.append(task)
        return jsonify({'message': 'Task created successfully'}, 201)
    else:
        return jsonify({'message': 'Title is required'}, 400)

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if task_id < len(tasks):
        data = request.get_json()
        if 'title' in data:
            tasks[task_id]['title'] = data['title']
            return jsonify({'message': 'Task updated successfully'})
        else:
            return jsonify({'message': 'Title is required'}, 400)
    else: 
        return jsonify({'message': 'Task not found'}, 404)
    
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id < len(tasks):
        del tasks[task_id]
        return jsonify({'message': 'Task deleted successfully'})
    else:
        return jsonify({'message': 'Task not found'}, 404)

if __name__ == '__main__':
    app.run()