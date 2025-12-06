from src.banco_dados import conectar
from src.repositorios import mercado_categoria_repositorio

def executar():
    # criar_categoria()
    listar_categorias()
    # editar_categorias()
    # apagar_categorias()

    print("Obrigado!")


def criar_categoria():
    nome = input("Digite o nome da nova categoria: ")

    mercado_categoria_repositorio.cadastrar(nome)

    print("Categoria criada com sucesso")


def listar_categorias():
    categorias = mercado_categoria_repositorio.obter_todos()

    # [] => Lista (é possível alterar)
    # {} => Dicionário (é possível alterar)
    # () => Tupla (somente leitura)

    for categoria in categorias:
        id = categoria["id"]

        nome = categoria["nome"]

        print("ID:", id, "\tNOME:", nome)


def editar_categorias():
    listar_categorias()

    id = input("Digite o ID que deseja editar: ")

    nome = input("Digite o novo nome: ")

    mercado_categoria_repositorio.editar(id, nome)

    print("Categoria alterada com sucesso")


def apagar_categorias():
    listar_categorias()

    id = input("Digite o ID que deseja apagar: ")

    linhas_afetadas = mercado_categoria_repositorio.apagar(id)

    if linhas_afetadas == 0:
        print("ID informado inexistente, tente novamente")
    else:
        print("Categoria apagada com sucesso")

