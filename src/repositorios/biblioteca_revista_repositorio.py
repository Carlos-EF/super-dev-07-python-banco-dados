from src.banco_dados import conectar_biblioteca


def obter_todos():
    conexao = conectar_biblioteca()

    cursor = conexao.cursor()

    sql = "SELECT id, titulo, edicao, data_publicacao, editora FROM revistas"

    cursor.execute(sql)

    registros = cursor.fetchall()

    conexao.close()

    cursor.close()

    revistas = []
    
    for registro in registros:
        revista = {
            "id": registro[0],
            "titulo": registro[1],
            "edicao": registro[2],
            "data_publicacao": registro[3],
            "editora": registro[4],
        }

        revistas.append(revista)

    return revistas