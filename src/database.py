import sqlite3
from datetime import datetime

DATABASE = "tarefas.db"


def conectar():
    conexao = sqlite3.connect(DATABASE)
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            responsavel TEXT,
            status TEXT,
            prioridade TEXT DEFAULT 'Média',
            data_criacao TEXT
        )
    """)

    conexao.commit()

    cursor.execute("PRAGMA table_info(tarefas)")
    colunas = [coluna[1] for coluna in cursor.fetchall()]

    if "prioridade" not in colunas:
        cursor.execute("""
            ALTER TABLE tarefas
            ADD COLUMN prioridade TEXT DEFAULT 'Média'
        """)
        conexao.commit()

    conexao.close()


def adicionar_tarefa(titulo, descricao, responsavel, prioridade):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO tarefas
        (titulo, descricao, responsavel, status, prioridade, data_criacao)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        titulo,
        descricao,
        responsavel,
        "A Fazer",
        prioridade,
        datetime.now().strftime("%d/%m/%Y %H:%M")
    ))

    conexao.commit()
    conexao.close()


def listar_tarefas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM tarefas ORDER BY id DESC")

    tarefas = cursor.fetchall()

    conexao.close()

    return tarefas


def buscar_tarefa(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM tarefas WHERE id=?", (id,))
    tarefa = cursor.fetchone()

    conexao.close()

    return tarefa


def atualizar_tarefa(id, titulo, descricao, responsavel, prioridade):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE tarefas
        SET titulo=?,
            descricao=?,
            responsavel=?,
            prioridade=?
        WHERE id=?
    """, (
        titulo,
        descricao,
        responsavel,
        prioridade,
        id
    ))

    conexao.commit()
    conexao.close()


def excluir_tarefa(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM tarefas WHERE id=?", (id,))

    conexao.commit()
    conexao.close()


def alterar_status(id, status):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE tarefas SET status=? WHERE id=?",
        (status, id)
    )

    conexao.commit()
    conexao.close()