from flask import Flask, request, jsonify
from models.task import task  
app = Flask(__name__)

#CRUD:create, read, update and  delete = criar, ler, atulizar, e deletar
#tabela : tarefa 

tasks = []
task_id_control = 1

@app.route("/tasks",methods=["POST"])
def create_tasks():
    global task_id_control
    data = request.get_json()
    new_tasks = task(id=task_id_control ,title=data.get("title"),description=data.get("description",""))
    task_id_control += 1
    tasks.append(new_tasks)
    print(tasks)
    return jsonify({"menssage":"nova tarefa criada com sucesso","id": new_tasks.id})

@app.route("/tasks",methods=["GET"])
def get_tasks():
    tasks_list = [task.to_dict() for task in tasks]
  

    output = {"tasks": [
tasks_list],
    "total_tasks":len(tasks_list)
    }
    return jsonify(output)

@app.route("/tasks/<int:id>",methods=["GET"])
def get__task(id):
    task = None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({"menssagem":"ao foi possivel encontra atividade "}), 404

@app.route("/tasks/<int:id>",methods=["PUT"])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
            
    print(task)
    if task == None:
        return jsonify({"menssagem":"ao foi possivel encontra atividade "}), 404
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completada = data['completada']
    print(task)
    return jsonify({"menssagem":"tarefa completada com sucesso"})

@app.route("/tasks/<int:id>",methods=["DELETE"])
def delete_taks(id):
    task = None
    for  t in tasks:
        if t.id == id:
            task = t
            break
    
    if task == None:
        return jsonify({"menssagem":"tarefa nao encontrada"}), 404
    
    tasks.remove(task)
    return jsonify({"menssagem":"tarefa deletada"})





if __name__ == "__main__":
    app.run(debug=True)

