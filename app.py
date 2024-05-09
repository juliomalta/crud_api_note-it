from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({'message': 'Tarefa criada com sucesso!'}), 201
# O método get_json() é usado para pegar os dados enviados no corpo da requisição, e o segundo método get() é usado para pegar os dados do dicionário data, se não existir, ele retorna um valor padrão, que é uma string vazia. O title entretanto, é obrigatório, por isso não tem um valor padrão.

@app.route('/tasks', methods=['GET'])
def list_tasks():
    tasks_dict = [task.to_dict() for task in tasks]

    output = {
        'tasks': tasks_dict,
        'total': len(tasks_dict)
    }
    return jsonify(output)
#     task_list = []
#     for task in tasks:
#         task_list.append(task.to_dict())

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for task in tasks:
        if task.id == id:
            return jsonify(task.to_dict())
    return jsonify({'message': 'Tarefa não encontrada!'}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    for task in tasks:
        if task.id == id:
            task.title = data['title']
            task.description = data.get('description', task.description)
            task.status = data.get('status', task.status)
            return jsonify({'message': 'Tarefa atualizada com sucesso!'})
    return jsonify({'message': 'Tarefa não encontrada!'}), 404

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    target_task = None
    for task in tasks:
        if task.id == id:
            target_task = task
            break
    if target_task is not None:
        tasks.remove(target_task)
        return jsonify({'message': 'Tarefa deletada com sucesso!'})
    return jsonify({'message': 'Tarefa não encontrada!'}), 404

# Reparar que evitei fazer a remoção dentro da iteração, pois pode causar erros, alterando o tamanho da lista, por exemplo.

if __name__ == '__main__':
    app.run(debug=True) 
# Este if é usado para rodar o servidor localmente, se o arquivo for importado em outro arquivo, o servidor não será iniciado.