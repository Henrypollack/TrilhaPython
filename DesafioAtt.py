import textwrap

def menu (): 
    menu = """\n
================= M E N U ==============

[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[nc]\tNova conta
[lc]\tListar Contas     
[nu]\tNovo usario
[q]\tSair

=> """
    return input(textwrap.dedent(menu))

def depositar(saldo,valor,extrato, /):
     if valor > 0:
          saldo += valor
          extrato += f"Deposito:\tR$ {valor:.2f}\n"
          print("\n=== Deposito realizado com sucesso! ===")
     else:
          print("\n@@@ Operação Falhou! O valor informado é invalido @@@")
     return saldo,extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
            print('\033[31m @@@ Operação falhou! Você não tem saldo suficiente. @@@ \033[m')

    elif excedeu_limite:
        print("\033[31m @@@ Operação falhou! O valor do saque excede o limite. @@@ \033[m")

    elif excedeu_saques:
        print("\033[31m @@@ Operação falhou! Número máximo de saques excedido. @@@ \033[m")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\033[32m === Saque Realizado Com sucesso! ===\033[m" )

    else:
        print("\033[31m Operação falhou! O valor informado é inválido.\033[m")
    return saldo, extrato

def exebir_extrato(saldo,/,*,extrato):    
    msg = "EXTRATO"
    msg2="="
    print(msg.center(42,"="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print(msg2.center(43,"="))

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numero): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n\033[31m@@@ Ja existe usuario com esse CPF! @@@\033[m")
        return
        
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaa): ")
    endereco = input("Informe o seu endereço (logadouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome":nome,"data_nascimento":data_nascimento,"cpf":cpf,"enderecos":endereco})

    print("\033[32m=== Usuario criado com sucesso! ===\033[m")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("\033[32m===Conta criada com sucesso!===\033[m")
        return{"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
    
    print("\033[31m@@@ Usuario não encontrado, fluxo de criação de conta encerrado! @@@\033[m ")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados=[usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        print("="*60)
        print(textwrap.dedent(linha))

def main():
    AGENCIA = "001"
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios =[]
    contas = []

    while True:
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("\033[33m Informe o valor do deposito:\033[m"))
            
            saldo,extrato = depositar(saldo,valor,extrato)

        elif opcao == "s":
            valor = float(input("\033[33m Informe o valor do saque:\033[m "))

            saldo,extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )    
        elif opcao == "e":
            exebir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta=len(contas) +1
            conta = criar_conta(AGENCIA,numero_conta,usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)         

        elif opcao == "q":
            break

        else:
            print('\033[31m Operação inválida, por favor selecione novamente a operação desejada.\033[m')
        
main ()
        