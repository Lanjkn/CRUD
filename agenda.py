AGENDA = {}


def mostraContatos():
    if(AGENDA):
        for contato in AGENDA:
            buscaContatos(contato)
    else:
        print("Agenda Vazia.")


def buscaContatos(contatoProcurado):
        try:
            print(contatoProcurado, ":\n Telefone:", AGENDA[contatoProcurado]['telefone'], "\n Email:", AGENDA[contatoProcurado]["email"], "\n Endereço:", AGENDA[contatoProcurado]["endereco"])
        except KeyError as e:
            print("Contato {} não encontrado!".format(e))
        except Exception as e:
            print("Algum erro ocorreu. {}".format(e))



def inserirContato(contato, telefone, email, endereco):
    try:
        AGENDA[contato] = {
        "telefone":telefone,
        "email":email,
        "endereco":endereco,
        }
    except Exception as e:
        print("Erro: {}".format(e))


def editarContato(contato):
    try:
        # This is only to test if the contact actually exists. / Apenas para checar se o contato existe de fato!
        AGENDA[contato]
    except KeyError:
        print("Contato {} não existente.".format(contato))
        return
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
    try:
        AGENDA.pop(contato)
    except KeyError as e:
        print("Contato {} não existe!".format(e))

        
def menu():
    print("O que deseja fazer?: ")
    print("1 - Adicionar Contato")
    print("2 - Excluir Contato")
    print("3 - Alterar dados de Contato")
    print("4 - Buscar Contato")
    print("5 - Mostrar lista de Contatos")
    print("0 - Sair")


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
        excluirContato(contatoExcluir)
        
    elif(acao == "3"):
        contatoEditar = input("Qual contato deseja editar?: ")
        editarContato(contatoEditar)
    elif(acao == "4"):
        contatoBusca = input("Qual o nome do seu contato?: ")
        buscaContatos(contatoBusca)
    elif(acao == "5"):
        mostraContatos()
    elif(acao == "0"):
        break
    else:
        print("Opção inválida")
