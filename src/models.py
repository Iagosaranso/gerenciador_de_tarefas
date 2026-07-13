from dataclasses import dataclass
from datetime import datetime

@dataclass
class Tarefa:
    id: int
    titulo: str
    descricao: str
    responsavel: str
    status: str
    data_criacao: str

    @staticmethod
    def criar(id, titulo, descricao, responsavel):
        return Tarefa(
            id=id,
            titulo=titulo,
            descricao=descricao,
            responsavel=responsavel,
            status="A Fazer",
            data_criacao=datetime.now().strftime("%d/%m/%Y %H:%M")
        )