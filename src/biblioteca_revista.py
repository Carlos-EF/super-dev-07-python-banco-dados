from mysql.connector import connect


def executar_biblioteca_revista():
    # listar_revistas()

    cadastrar_revista()


def listar_revistas():
    conexao = connect(
        user="root",
        password="admin",
        database="biblioteca",
        port="3306",
        host="127.0.0.1"
    )

    cursor = conexao.cursor()

    sql = "SELECT id, titulo, edicao, data_publicacao, editora FROM revistas"

    cursor.execute(sql)

    registros = cursor.fetchall()

    conexao.close()

    cursor.close()

    for registro in registros:
        id = registro[0]

        titulo = registro[1]
        
        edicao = registro[2]

        data_publicacao = registro[3]

        editora = registro[4]

        print("ID:", id, "\tTÍTULO:", titulo, "\tEDIÇÂO:", edicao, "\tDATA DE PUBLICAÇÂO:", data_publicacao, "\tEDITORA:", editora)


def cadastrar_revista():
    listar_revistas()

    titulo = input("Digite o título da revista: ")

    edicao = input("Digite a edição da revista: ")

    data_publicacao = input("Digite a data de publicação: ")

    editora = input("Digite a editora da revista: ")

    conexao = connect(
        port="3306",
        host="127.0.0.1",
        password="admin",
        user="root",
        database="biblioteca",
    )

    cursor = conexao.cursor()

    sql = "INSERT INTO revistas (titulo, edicao, data_publicacao, editora) VALUES (%s, %s, %s, %s)"

    dados = (titulo, edicao, data_publicacao, editora)

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()

    conexao.close()

    print("Revista modificada com sucesso!")


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
        print("Ocorreu um erro ao tentar apagar a revista.")