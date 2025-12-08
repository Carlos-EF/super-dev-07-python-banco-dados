from src.repositorios import mercado_produto_repositorio


def executar_produtos():
    # cadastrar_produto()
    # apagar_produto()
    listar_produtos()


def cadastrar_produto():
    nome = input("Digite o nome do novo produto: ")

    id_categoria = int(input("Digite o ID da categoria: "))

    mercado_produto_repositorio.cadastrar(nome, id_categoria)

    print("Produto cadastrado com sucesso!")


def apagar_produto():
    id = int(input("Digite o ID do produto que deseja apagar: "))

    linhas_afetadas = mercado_produto_repositorio.apagar(id)

    if linhas_afetadas:
        print("Produto apagagado com sucesso!")
    else:
        print("Não foi possível apagar o produto.")



def listar_produtos():
    produtos = mercado_produto_repositorio.obter_todos()

    print("Código".ljust(8, " "), "Nome".ljust(20, " "), "Categoria")

    for produto in produtos:
        print(
            str(produto["id"]).ljust(8, " "),
            produto["nome"].ljust(20, " "),
            produto["categoria"]["nome"]
        )
