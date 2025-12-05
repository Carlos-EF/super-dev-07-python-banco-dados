from mysql.connector import connect


def executar_biblioteca_revista():
    listar_revistas()


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