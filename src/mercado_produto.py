from src.repositorios import mercado_produto_repositorio


def executar_produtos():
    cadastrar_produto()


def cadastrar_produto():
    nome = input("Digite o nome do novo produto: ")

    id_categoria = int(input("Digite o ID da categoria: "))

    mercado_produto_repositorio.cadastrar(nome, id_categoria)

    print("Produto cadastrado com sucesso!")