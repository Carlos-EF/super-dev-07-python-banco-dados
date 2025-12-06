from src.repositorios import biblioteca_manga_repositorio


# 14.   MySQL Criar uma tabela de mangas com as colunas: id, nome, volume, autor, data de lançamento
# 15.   MySQL Criar registro na tabela de mangas do Naruto Volume 52
# 16.   MySQL Criar registro na tabela de mangas do Dragon Ball Volume 20
# 17.   Criar a função de listar
# 18.   Criar a função de editar
# 18.   Criar a função de apagar
# 19.   Criar a função de cadastrar 


def executar_biblioteca_mangas():
    # listar_mangas()
    # editar_manga()
    apagar_manga()
    # cadastrar_manga()


def listar_mangas():
    mangas = biblioteca_manga_repositorio.obter_todos()

    for manga in mangas:
        id = manga["id"]

        nome = manga["nome"]

        volume = manga["volume"]

        autor = manga["autor"]

        data_lancamento = manga["data_lancamento"]

        print("ID:", id, "\tNOME:", nome, "\tVOLUME:", volume, "\tAUTOR:", autor, "\tDATA DE LANÇAMENTO:", data_lancamento)


def editar_manga():
    listar_mangas()

    id = input("Digite o ID do mangá que deseja editar: ")

    nome = input("Digite o nome do mangá: ")

    volume = input("Digite o volume: ")

    autor = input("Digite o autor do manga: ")

    data_lancamento = input("Digite a data de lançamento do volume: ")

    linhas_modificadas = biblioteca_manga_repositorio.editar(id, nome, volume, autor, data_lancamento)

    if linhas_modificadas == 0:
        print("Ocorreu um erro ao tentar editar o mangá.")
    else:
        print("Mangá alterado com sucesso!")


def apagar_manga():
    listar_mangas()

    id = input("Digite o ID do mangá que deseja apagar: ")

    linhas_apagadas = biblioteca_manga_repositorio.apagar(id)

    if linhas_apagadas == 0:
        print("Ocorreu um erro ao tentar apagar o mangá.")
    else:
        print("Mangá apagado com sucesso!")


def cadastrar_manga():
    nome = input("Digite o nome do mangá: ")

    volume = input("Digite o volume do mangá: ")

    autor = input("Digite o autor do mangá: ")

    data_lancamento = input("Digite a data de lançamento do volume: ")

    biblioteca_manga_repositorio.cadastrar(nome, volume, autor, data_lancamento)

    print(f"Mangá '{nome}' cadastrado com sucesso!")

