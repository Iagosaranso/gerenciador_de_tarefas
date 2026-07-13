from flask import Flask, render_template, request, redirect
from src.database import (
    criar_tabela,
    adicionar_tarefa,
    listar_tarefas,
    buscar_tarefa,
    atualizar_tarefa,
    excluir_tarefa,
    alterar_status
)

app = Flask(__name__)

criar_tabela()


@app.route("/")
def inicio():
    tarefas = listar_tarefas()
    return render_template("index.html", tarefas=tarefas)


@app.route("/adicionar", methods=["POST"])
def adicionar():

    adicionar_tarefa(
        request.form["titulo"],
        request.form["descricao"],
        request.form["responsavel"],
        request.form["prioridade"]
    )

    return redirect("/")


@app.route("/editar/<int:id>")
def editar(id):

    tarefa = buscar_tarefa(id)

    return render_template("editar.html", tarefa=tarefa)


@app.route("/atualizar/<int:id>", methods=["POST"])
def atualizar(id):

    atualizar_tarefa(
        id,
        request.form["titulo"],
        request.form["descricao"],
        request.form["responsavel"],
        request.form["prioridade"]
    )

    return redirect("/")


@app.route("/excluir/<int:id>")
def excluir(id):

    excluir_tarefa(id)

    return redirect("/")


@app.route("/status/<int:id>/<status>")
def status(id, status):

    alterar_status(id, status)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)