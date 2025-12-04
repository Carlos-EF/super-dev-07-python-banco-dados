from mysql.connector import connect

def executar_biblioteca():
    # cadastrar_livro()
    editar_livro()
    # apagar_livro()
    # listar_livros()


def cadastrar_livro():
    titulo = input("Digite o título do livro que deseja cadastrar: ")

    conexao = connect(
        user="root",
        password="admin",
        database="biblioteca",
        host="127.0.0.1",
        port="3306",
    )

    cursor = conexao.cursor()

    sql = "INSERT INTO livros (titulo) VALUE (%s)"

    dados = (titulo,)

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()

    conexao.close()

    print(f"Livro {titulo} cadastrado com sucesso!")


def editar_livro():
    listar_livros()

    id = input("Digite o id do livro que deseja editar: ")

    titulo = input("Digite o novo título do livro: ")

    conexao = connect(
        password="admin",
        user="root",
        host="127.0.0.1",
        port="3306",
        database="biblioteca",
    )

    cursor = conexao.cursor()

    sql = "UPDATE livros SET titulo= %s WHERE id = %s"

    dados = (titulo, id)

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()

    conexao.close()

    print("Livro alterado com sucesso!")


def apagar_livro():
    listar_livros()

    id = input("Digite o ID que deseja apagar: ")

    conexao = connect(
        user="root",
        password="admin",
        port="3306",
        host="127.0.0.1",
        database="biblioteca",
    )

    cursor = conexao.cursor()

    sql = "DELETE FROM livros WHERE id = %s"

    dados = (id,)

    cursor.execute(sql, dados)

    conexao.commit()

    conexao.close()

    cursor.close()

    linhas_afetadas = cursor.rowcount

    if linhas_afetadas == 0:
        print("Ocorreu um erro ao tentar apagar o livro.")
        return
    else:
        print("Livro apagado com sucesso!")


def listar_livros():
    conexao = connect(
        user="root",
        password="admin",
        database="biblioteca",
        host="127.0.0.1",
        port="3306",
    )

    cursor = conexao.cursor()

    sql = "SELECT id, titulo FROM livros"

    cursor.execute(sql)

    registros = cursor.fetchall()

    cursor.close()

    conexao.close()

    for registro in registros:
        id = registro[0]

        titulo = registro[1]

        print("ID:", id, "\tTITULO:", titulo)