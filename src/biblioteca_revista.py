from mysql.connector import connect
from src.repositorios import biblioteca_revista_repositorio


def executar_biblioteca_revista():
    listar_revistas()

    # cadastrar_revista()


def listar_revistas():
    revistas = biblioteca_revista_repositorio.obter_todos()

    for revista in revistas:
        id = revista["id"]

        titulo = revista["titulo"]
        
        edicao = revista["edicao"]

        data_publicacao = revista["data_publicacao"]

        editora = revista["editora"]

        print("ID:", id, "\tTÍTULO:", titulo, "\tEDIÇÂO:", edicao, "\tDATA DE PUBLICAÇÂO:", data_publicacao, "\tEDITORA:", editora)


def cadastrar_revista():
    titulo = input("Digite o título da revista: ")

    edicao = input("Digite a edição da revista: ")

    data_publicacao = input("Digite a data de publicação: ")

    editora = input("Digite a editora da revista: ")

    biblioteca_revista_repositorio.cadastrar(titulo, edicao, data_publicacao, editora)

    print("Revista cadastrada com sucesso com sucesso!")


def apagar_revista():
    listar_revistas()

    id = input("Digite o ID da revista que deseja apagar: ")

    conexao = connect(
        user="root",
        password="admin",
        port="3306",
        host="127.0.0.1",
        database="biblioteca"
    )

    sql = "DELETE FROM revistas WHERE id= %s"

    dados = (id, )

    cursor = conexao.cursor()

    cursor.execute(sql, dados)

    conexao.commit()

    linhas_apagadas = cursor.rowcount

    cursor.close()

    conexao.close()

    if linhas_apagadas == 0:
        print("Ocorreu um erro ao tentar apagar a revista.")
    else:
        print("Revista apagada com sucesso!")