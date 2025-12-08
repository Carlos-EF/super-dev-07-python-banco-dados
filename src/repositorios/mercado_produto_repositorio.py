from src.banco_dados import conectar


def cadastrar(nome: str, id_categoria: int):
    conexao = conectar()

    cursor = conexao.cursor()

    sql = "INSERT INTO produtos (nome, id_categoria) VALUES (%s, %s)"

    dados = (nome, id_categoria)

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()

    conexao.close()


def editar():
    pass


def apagar():
    pass


def obter_todos():
    pass