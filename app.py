from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tarefas = []


@app.route("/")
def inicio():
    return render_template("index.html", tarefas=tarefas)


@app.route("/adicionar", methods=["POST"])
def adicionar():

    tarefa = {
        "titulo": request.form["titulo"],
        "descricao": request.form["descricao"],
        "responsavel": request.form["responsavel"]
    }

    tarefas.append(tarefa)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)