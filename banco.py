def menu_principal():
    num_conta = 0
    while True:
        print("\n############ MENU PRINCIPAL ############")
        print("1. Criar Conta      2. Mostrar Saldo")
        print("3. Depósito         4. Saque")
        print("5. Transferência    6. Relatório Geral")
        print("0. Sair")
        print("---------------------------------------")
        op = int(input("Digite sua opção -> "))
        if op == 0:
            break
        elif op == 1:
            print("#### CRIANDO UMA CONTA ####")
            num_conta += 1
            nome = input("Nome do cliente: ")
            valor = float(input("Saldo inicial: "))
            criar_ac(nome,valor,num_conta)
            #conta.append(criar(num_conta, nome, valor, 500.00))
        elif op == 2:
            print("##### SALDO EM CONTA #####")
            numero = int(input("Número da conta: "))
            mostrar_saldo(lista_contas,numero)
            #mostrar_saldo(conta, numero)
        elif op == 3:
            print("#### DEPÓSITO EM CONTA ####")
            numero = int(input("Número da conta: "))
            valor = float(input("Valor a depositar: "))
            deposito(lista_contas, numero, valor)
            #creditar(conta, numero, valor)
        elif op == 4:
            print("##### SAQUE EM CONTA #####")
            numero = int(input("Número da conta: "))
            valor = float(input("Valor a sacar: "))
            saque(lista_contas, numero, valor)
            #debitar(conta, numero, valor)
        elif op == 5:
            print("### TRANSFERÊNCIA ENTRE CONTAS ###")
            num1 = int(input("Número da conta de origem: "))
            num2 = int(input("Número da conta de destino: "))
            valor = float(input("Valor a transferir: R$ "))
            transferir(lista_contas,num1,num2,valor)
            #transferir(conta, num1, num2, valor)
        elif op == 6:
            print("## RELATÓRIO DE CONTAS ##")
            rel(lista_contas)
            #emitir_relatorio(conta)
        else:
            print("\n##### OPÇÃO INVÁLIDA #####\n")

lista_contas = []


def criar_ac(nome,valor,nume):
    contas = {}
    lista_contas.append(contas)
    contas[nome] = valor
    contas['numero'] = nume
    print(contas)
    print(lista_contas)


def mostrar_saldo(lis,con):
    for i in lis[con-1].values():
        print(f"O saldo da conta {lis[con-1]['numero']} é {i}")
        break


def deposito(lis,con,val):
    for i,j in lis[con - 1].items():
        lis[con - 1][i] += val
        break
    print(lista_contas)


def saque(lis,con,val):
    for i,j in lis[con - 1].items():
        lis[con - 1][i] -= val
        break
    print(lista_contas)


def transferir(lis,num1,num2,val):
    for i,j in lis[num1 - 1].items():
        lis[num1 - 1][i] -= val
        break
    for i, j in lis[num2 - 1].items():
        lis[num2 - 1][i] += val
        break
    print(lista_contas)


def rel(a):
    ind = 0
    test = 0
    for i in a:
        test += 1
    while ind < test:
        for i,j in a[ind].items():
            print(f"Conta de {i} tem saldo {j}")
            break
        ind += 1


if __name__ == "__main__":
    menu_principal()
