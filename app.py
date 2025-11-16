from flask import Flask, request
from models.task import task  
app = Flask(__name__)

#CRUD:create, read, update and  delete = criar, ler, atulizar, e deletar
#tabela : tarefa 

tasks = []


@app.route("/tasks",methods=["POST"])
def create_tasks():
    data = request.get_json()
    print(data)
    return "teste"



if __name__ == "__main__":
    app.run(debug=True)

