def menu():
    print("\n=== BIBLIOTECA ===")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Sair")


while True:
    menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Cadastrar livro")

    elif opcao == "2":
        print("Listar livros")

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida")