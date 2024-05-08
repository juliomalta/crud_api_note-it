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
    return jsonify({'message': 'Task created successfully!'}), 201
# O método get_json() é usado para pegar os dados enviados no corpo da requisição, e o segundo método get() é usado para pegar os dados do dicionário data, se não existir, ele retorna um valor padrão, que é uma string vazia. O title entretanto, é obrigatório, por isso não tem um valor padrão.

if __name__ == '__main__':
    app.run(debug=True) 
# Este if é usado para rodar o servidor localmente, se o arquivo for importado em outro arquivo, o servidor não será iniciado.