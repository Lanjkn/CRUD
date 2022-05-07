AGENDA = {}

def verificaContatos(contato):
    for contatos in AGENDA:
        if(contato == contatos):
            return True
        else:
            return False   

def mostraContatos():
    for contato in AGENDA:
        buscaContatos(contato)


def buscaContatos(contatoProcurado):
    contatoEncontrado = False
    for contato in AGENDA:
        if(contatoProcurado == contato):
            print(contato, ":\n Telefone:", AGENDA[contato]['telefone'], "\n Email:", AGENDA[contato]["email"], "\n Endereço:", AGENDA[contato]["endereco"])
            contatoEncontrado = True
    if(contatoEncontrado == False):
        print("Contato não encontrado.")


def inserirContato(contato, telefone, email, endereco):
    AGENDA[contato] = {
    "telefone":telefone,
    "email":email,
    "endereco":endereco,
    }


def editarContato(contato):
    print("O que deseja editar?")
    print("1 - Telefone")
    print("2 - Email")
    print("3 - Endereco")
    print("4 - Todos")
    acao = input()
    if(acao == "1"):
        telefone = input("Digite o novo telefone: ")
        AGENDA[contato]['telefone'] = telefone
    elif(acao == "2"):
        email = input("Digite o novo Email: ")
        AGENDA[contato]['email'] = telefone
    elif(acao == "3"):
        endereco = input("Digite o novo Endereço: ")
        AGENDA[contato]['endereco'] = endereco
    elif(acao == "4"):
        telefone = input("Digite o novo telefone: ")
        email = input("Digite o novo Email: ")
        endereco = input("Digite o novo Endereço: ")   
        AGENDA[contato]['telefone'] = telefone
        AGENDA[contato]['email'] = email
        AGENDA[contato]['endereco'] = endereco
    else:
        print("Opção não existente.")


def excluirContato(contato):
    AGENDA.pop(contato)

def menu():
    print("O que deseja fazer?: ")
    print("1 - Adicionar Contato")
    print("2 - Excluir Contato")
    print("3 - Alterar dados de Contato")
    print("4 - Buscar Contato")
    print("5 - Mostrar lista de Contatos")
    print("6 - Sair")



while True: 
    menu()
    acao = input("O que deseja fazer?: ")
    if(acao == "1"):
        contatoNovo = input("Digite o nome do contato: ")
        print("Perfeito!")
        novoTelefone = input("Digite o telefone do contato: ")
        novoEmail = input("Digite o email do contato: ")
        novoEndereco = input("Digite o endereco do contato: ")
        inserirContato(contatoNovo, novoTelefone, novoEmail, novoEndereco)
        print("Contato {} inserido!".format(contatoNovo))
    elif(acao == "2"):
        contatoExcluir = input("Qual contato deseja excluir?: ") 
        if (verificaContatos(contatoExcluir)):
            excluirContato(contatoExcluir)
        else:
            print("Contato Inexistente!")
    elif(acao == "3"):
        contatoEditar = input("Qual contato deseja editar?: ")
        if (verificaContatos(contatoEditar)):
            editarContato(contatoEditar)
        else:
            print("Contato inexistente!")
    elif(acao == "4"):
        contatoBusca = input("Qual o nome do seu contato?: ")
        buscaContatos(contatoBusca)
    elif(acao == "5"):
        mostraContatos()
    elif(acao == "6"):
        break
    else:
        print("Opção inválida")
