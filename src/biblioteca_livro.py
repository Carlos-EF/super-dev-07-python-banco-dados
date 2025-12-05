from mysql.connector import connect

def executar_biblioteca():
    # cadastrar_livro()
    # editar_livro()
    # apagar_livro()
    # listar_livros()

    # listar_mangas()
    # editar_manga()
    apagar_manga()


def cadastrar_livro():
    titulo = input("Digite o título do livro que deseja cadastrar: ")

    quantidade_paginas = input("Digite a quantidade de páginas do livro: ")

    autor = input("Digite o nome do autor do livro: ")

    preco = input("Digite o preço do livro: ")

    isbn = input("Digite o ISBN do livro: ")

    descricao = input("Digite a descrição do livro: ")

    conexao = connect(
        user="root",
        password="admin",
        database="biblioteca",
        host="127.0.0.1",
        port="3306",
    )

    cursor = conexao.cursor()

    sql = "INSERT INTO livros (titulo, quantidade_paginas, autor, preco, isbn, descricao) VALUE (%s, %s, %s, %s, %s, %s)"

    dados = (titulo, quantidade_paginas, autor, preco, isbn, descricao)

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()

    conexao.close()

    print(f"Livro {titulo} cadastrado com sucesso!")


def editar_livro():
    listar_livros()

    id = input("Digite o id do livro que deseja editar: ")

    titulo = input("Digite o novo título do livro: ")

    quantidade_paginas = input("Digite a nova quantidade de páginas do livro: ")

    autor = input("Digite o autor do livro: ")

    preco = input("Digite o preço do livro: ")

    isbn = input("Digite o ISBN do livro: ")

    descricao = input("Digite uma breve descrição do livro: ")

    conexao = connect(
        password="admin",
        user="root",
        host="127.0.0.1",
        port="3306",
        database="biblioteca",
    )

    cursor = conexao.cursor()

    sql = "UPDATE livros SET titulo= %s, quantidade_paginas= %s, autor= %s, preco= %s, isbn= %s, descricao= %s WHERE id = %s"

    dados = (titulo, quantidade_paginas, autor, preco, isbn, descricao, id)

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()

    conexao.close()

    linhas_alteradas = cursor.rowcount

    if linhas_alteradas == 0:
        print("Ocorreu um erro ao tentar alterar o livro.")
    else:
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

    sql = "SELECT id, titulo, quantidade_paginas, autor, preco, isbn, descricao FROM livros"

    cursor.execute(sql)

    registros = cursor.fetchall()

    cursor.close()

    conexao.close()

    for registro in registros:
        id = registro[0]

        titulo = registro[1]

        quantidade_paginas = registro[2]

        autor = registro[3]

        preco = registro[4]

        isbn = registro[5]

        descricao = registro[6]

        print("ID:", id, "\tTITULO:", titulo, "\tPÁGINAS:", quantidade_paginas, "\tAUTOR:", autor, "\tPRECO:", preco, "\tISBN:", isbn, "\tDESCRIÇÂO:", descricao)


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



# 14.   MySQL Criar uma tabela de mangas com as colunas: id, nome, volume, autor, data de lançamento
# 15.   MySQL Criar registro na tabela de mangas do Naruto Volume 52
# 16.   MySQL Criar registro na tabela de mangas do Dragon Ball Volume 20
# 17.   Criar a função de listar
# 18.   Criar a função de editar
# 18.   Criar a função de apagar
# 19.   Criar a função de cadastrar  

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