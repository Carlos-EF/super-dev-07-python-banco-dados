from mysql.connector import connect


# 14.   MySQL Criar uma tabela de mangas com as colunas: id, nome, volume, autor, data de lançamento
# 15.   MySQL Criar registro na tabela de mangas do Naruto Volume 52
# 16.   MySQL Criar registro na tabela de mangas do Dragon Ball Volume 20
# 17.   Criar a função de listar
# 18.   Criar a função de editar
# 18.   Criar a função de apagar
# 19.   Criar a função de cadastrar 


def executar_biblioteca_mangas():
    listar_mangas()
    # editar_manga()
    # apagar_manga()
    # cadastrar_manga()


def listar_mangas():
    conexao = connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="admin",
        database="biblioteca",
    )

    cursor = conexao.cursor()

    sql = "SELECT id, nome, volume, autor, data_lancamento FROM mangas"
    
    cursor.execute(sql)

    registros = cursor.fetchall()

    conexao.close()

    cursor.close()


    for registro in registros:
        id = registro[0]

        nome = registro[1]

        volume = registro[2]

        autor = registro[3]

        data_lancamento = registro[4]

        print("ID:", id, "\tNOME:", nome, "\tVOLUME:", volume, "\tAUTOR:", autor, "\tDATA DE LANÇAMENTO:", data_lancamento)


def editar_manga():
    listar_mangas()

    id = input("Digite o ID do mangá que deseja editar: ")

    nome = input("Digite o nome do mangá: ")

    volume = input("Digite o volume: ")

    autor = input("Digite o autor do manga: ")

    data_lancamento = input("Digite a data de lançamento do volume: ")

    conexao = connect(
        user="root",
        password="admin",
        host="127.0.0.1",
        port="3306",
        database="biblioteca",
    )

    dados = (nome, volume, autor, data_lancamento, id)

    sql = "UPDATE mangas SET nome=%s, volume= %s, autor= %s, data_lancamento= %s WHERE id= %s"

    cursor = conexao.cursor()

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()

    conexao.close()

    linhas_modificadas = cursor.rowcount
    if linhas_modificadas == 0:
        print("Ocorreu um erro ao tentar editar o mangá.")
    else:
        print("Mangá alterado com sucesso!")


def apagar_manga():
    listar_mangas()

    id = input("Digite o ID do mangá que deseja apagar: ")

    conexao = connect(
        password="admin",
        user="root",
        database="biblioteca",
        port="3306",
        host="127.0.0.1"
    )

    sql = "DELETE FROM mangas WHERE id = %s"

    dados = (id, )

    cursor = conexao.cursor()

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()

    conexao.close()

    linhas_apagadas = cursor.rowcount
    if linhas_apagadas == 0:
        print("Ocorreu um erro ao tentar apagar o mangá.")
    else:
        print("Mangá apagado com sucesso!")


def cadastrar_manga():
    nome = input("Digite o nome do mangá: ")

    volume = input("Digite o volume do mangá: ")

    autor = input("Digite o autor do mangá: ")

    data_lancamento = input("Digite a data de lançamento do volume: ")

    conexao = connect(
        port="3306",
        user="root",
        database="biblioteca",
        host="127.0.0.1",
        password="admin"
    )

    cursor = conexao.cursor()

    sql = "INSERT INTO mangas (nome, volume, autor, data_lancamento) VALUES (%s, %s, %s, %s)"

    dados = (nome, volume, autor, data_lancamento)

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()

    conexao.close()


    print(f"Mangá '{nome}' cadastrado com sucesso!")

