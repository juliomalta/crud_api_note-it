import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'

tasks = []

def test_create_task():
  new_task = {
    'title': 'Tarefa de teste', 
    'description': 'Descrição da tarefa'
  }

  response = requests.post(f'{BASE_URL}/tasks', json=new_task)
  assert response.status_code == 201
  response_json = response.json()
  assert 'message' in response_json
  assert 'id' in response_json
  tasks.append(response_json['id'])

  response = requests.get(f'{BASE_URL}/tasks/{response_json['id']}')
  response_json = response.json()
  assert response_json['title'] == 'Tarefa de teste'

def test_read_single_task():
  task_id = tasks[0]
  response = requests.get(f'{BASE_URL}/tasks/{task_id}')
  assert response.status_code == 200
  response_json = response.json()
  assert task_id == response_json['id']

def test_read_multi_task():
  response = requests.get(f'{BASE_URL}/tasks')
  assert response.status_code == 200
  response_json = response.json()
  assert 'tasks' in response_json
  assert 'total' in response_json
  # assert response_json['tasks'] == 1 ; assim é para testar se a quantidade de tarefas é igual a 1, e não se tem tarefas em geral.


def test_update_task():
  task_id = tasks[0]
  payload = {
    'title': 'Tarefa de teste atualizada',
    'description': 'Descrição da tarefa atualizada',
    'status': True
  }
  
  response = requests.put(f'{BASE_URL}/tasks/{task_id}', json=payload)
  assert response.status_code == 200
  response_json = response.json()
  assert response_json['message'] == 'Tarefa atualizada com sucesso!'

# Verificação do conteúdo atualizado
  response = requests.get(f'{BASE_URL}/tasks/{task_id}')
  assert response.status_code == 200
  response_json = response.json()
  assert response_json['title'] == payload['title']
  assert response_json['description'] == payload['description']
  assert response_json['status'] == payload['status']

def test_delete_task():
  task_id = tasks[0]
  response = requests.delete(f'{BASE_URL}/tasks/{task_id}')
  assert response.status_code == 200

  response = requests.get(f'{BASE_URL}/tasks/{task_id}')
  assert response.status_code == 404

def test_error_handling():
  response = requests.get(f'{BASE_URL}/tasks/100')
  assert response.status_code == 404
  response_json = response.json()
  assert response_json['message'] == 'Tarefa não encontrada!'
