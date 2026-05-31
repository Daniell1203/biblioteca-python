livros = []

arquivo = open("livros.txt", "r", encoding="utf-8")

for linha in arquivo:
    livros.append(linha.strip())

arquivo.close()


def menu():
    print("\n=== BIBLIOTECA ===")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Remover livro")
    print("5 - Sair")


while True:
    menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        nome = input("Nome do livro: ")
        livros.append(nome)

        arquivo = open("livros.txt", "w", encoding="utf-8")

        for livro in livros:
            arquivo.write(livro + "\n")

        arquivo.close()

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

        remover = input("Livro para remover: ")

        if remover in livros:

            livros.remove(remover)

            arquivo = open("livros.txt", "w", encoding="utf-8")

            for livro in livros:
                arquivo.write(livro + "\n")

            arquivo.close()

            print("Livro removido")

        else:
            print("Livro não encontrado")

    elif opcao == "5":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida")