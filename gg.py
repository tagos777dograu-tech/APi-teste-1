import pytest
import requests


BASE_URL = "http://127.0.0.1:5000"
tasks = []


def teste_create_task():
    nem_task_data = {
        "title":"nova tarefa",
        "description": "vermeho"
    }
    response = requests.post(f"{BASE_URL}/tasks",json=nem_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "menssage" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])

def teste_read_task():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def test_get_test():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert "completada" in response_json
def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
    "completada": False,
    "description": "descriçao nova",
    "title": "titulo atulizado"
}
        response = requests.put(f"{BASE_URL}/tasks/{task_id}",json=payload)
        response.status_code == 200
        response_json = response.json()
        assert "menssagem" in response_json
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["title"] == payload["title"]
        assert response_json["description"] == payload["description"]
        assert response_json["completada"] == payload["completada"]

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        response.status_code == 200
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404
 