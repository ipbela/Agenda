import time

def agenda():
    contatos = {
        "isabela": {
            "Telefone": "19991147273",
            "Endereço": [
                "avenida dos pioneiros",
                "575"
            ]
        },
        "davi":{
            "Telefone": "12345678955",
            "Endereço": [
                "avenida das amoreiras",
                "425"
            ]
        },
        "favaro":{
            "Telefone": "23415263895",
            "Endereço": [
                "rua joaquim",
                "235"
            ]
        }
    }

    while True:
        try:
            print("---AGENDA---")
            opcao = int(input("Digite a opção que deseja selecionar: "
                              "\n1 - Ligar para um contato"
                              "\n2 - Cadastrar um novo contato"
                              "\n3 - Remover um contato"
                              "\n4 - Listar Contatos"
                              "\n5 - Sair\n"))

            if opcao == 1:
                ligar(contatos)
            elif opcao == 2:
                cadastrar(contatos)
            elif opcao == 3:
                remover(contatos)
            elif opcao == 4:
                listar(contatos)
            elif opcao == 5:
                print("Programa Finalizado!")
                exit()
            else:
                print("------------------------")
                print("Digite uma opção válida!")
                print("------------------------")

        except ValueError:
            print("--------------------------")
            print("Digite caracteres válidos!")
            print("--------------------------")

def ligar(contatos):
    print("---CONTATOS DA AGENDA---")

    for nome, infos in contatos.items():
        for chave, valor in infos.items():
            if chave == "Telefone":
                print(f"Nome: {nome}\nTelefone: {valor}\n")

    while True:
        contato = input("Digite o nome do contato para quem deseja ligar: ").lower()
        existe = 0
        for nome, infos in contatos.items():
            if contato == nome.lower():
                existe = 1
                cont = 0
                while cont <= 2:
                    print("Ligando...")
                    time.sleep(1)
                    cont += 1

                print("Sua chamada foi encaminhada para a caixa postal. Tente novamente mais tarde!")
                print("----------------------------------------------------------------------------")

        if existe == 0:
            print("-----------------------------------------------")
            print("Esse não é um contato válido. Digite novamente!")
            print("-----------------------------------------------")

        opcao = input("Deseja ligar novamente? (S/N)")

        if opcao == "S" or opcao == "s":
            ligar(contatos)
        elif opcao == "N" or opcao == "n":
            agenda()
        else:
            print("Digite somente uma das opções.")

def cadastrar(contatos):
    print("\n-----CADASTRO-----")

    while True:
        nome = input("Digite o nome da pessoa que deseja cadastrar: \n")
        if nome in contatos:
            print("-" * 50)
            print("Este contato já existe! Digite um contato novo.")
            print("-" * 50)
        else:
            break

    while True:
        telefone = input("\nDigite o telefone: ")
        if any(telefone == infos["Telefone"] for infos in contatos.values()):
            print("-" * 50)
            print(f"Este número de contato já existe. Digite um número novo.")
            print("-" * 50)
        else:
            break

    enderecoRua = input("\nDigite o nome da rua/avenida do endereço: ")
    enderecoNum = int(input("\nDigite o numero do endereço: "))

    contatos[nome] = {
        "Telefone": telefone,
        "Endereço": [
            enderecoRua,
            enderecoNum
        ]
    }

    print("---CONTATOS DA AGENDA---")
    for nome, infos in contatos.items():
        for chave, valor in infos.items():
            for c, v in infos.items():
                if chave == "Telefone" and c == "Endereço":
                    print(f"\nNome: {nome.lower()}\nTelefone: {valor}\nEndereço: {v}")
    print("-" * 50)

def remover(contatos):
    print("\n---CONTATOS DA AGENDA---")
    for nome, infos in contatos.items():
        for chave, valor in infos.items():
            for c, v in infos.items():
                if chave == "Telefone" and c == "Endereço":
                    print(f"\nNome: {nome.lower()}\nTelefone: {valor}\nEndereço: {v}")
    print("-" * 50)

    while True:
        nome_remover = input("Digite o nome do contato que deseja remover: \n")
        if nome_remover in contatos:
            nome_removido = contatos.pop(nome_remover)
            print("-" * 50)
            print(f"O contato {nome_remover} foi removido com sucesso!")
            print("-" * 50)
        else:
            print("-" * 50)
            print("Este contato não existe! Digite um contato válido.")
            print("-" * 50)
        break

    for nome, infos in contatos.items():
        for chave, valor in infos.items():
            for c, v in infos.items():
                if chave == "Telefone" and c == "Endereço":
                    print(f"\nNome: {nome.lower()}\nTelefone: {valor}\nEndereço: {v}")
    print("-" * 50)

def listar(contatos):
    print("\n---LISTANDO CONTATOS---")
    print("-----------------------")
    for nome, infos in contatos.items():
        for chave, valor in infos.items():
            for c, v in infos.items():
                if chave == "Telefone" and c == "Endereço":
                    print(f"Nome: {nome.lower()}\nTelefone: {valor}\nEndereço: {v}\n")
    print("-" * 50)


if __name__ == "__main__":
    agenda()
