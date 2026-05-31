livros = []


def menu():
    print("\n=== BIBLIOTECA ===")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Sair")


while True:
    menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do livro: ")
        livros.append(nome)

        print("Livro cadastrado!")

    elif opcao == "2":

        if len(livros) == 0:
            print("Nenhum livro cadastrado")

        else:
            print("\nLivros cadastrados:")

            for livro in livros:
                print(f"- {livro}")

    elif opcao == "3":

        busca = input("Digite o nome do livro: ")

        if busca in livros:
            print("Livro encontrado!")

        else:
            print("Livro não encontrado")

    elif opcao == "4":
        break