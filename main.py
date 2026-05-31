livros = []


def menu():
    print("\n=== BIBLIOTECA ===")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Sair")


while True:
    menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do livro: ")
        livros.append(nome)

        print("Livro cadastrado!")

    elif opcao == "2":
        print("Listar livros")

    elif opcao == "3":
        break