menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("\033[33m Informe o valor do deposito:\033[m"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            

        else:
            print("\033[31m Operação falhou! O valor informado é inválido.\033[m")

    elif opcao == "s":
        valor = float(input("\033[33m Informe o valor do saque:\033[m "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('\033[31m Operação falhou! Você não tem saldo suficiente.\033[m')

        elif excedeu_limite:
            print("\033[31m Operação falhou! O valor do saque excede o limite.\033[m")

        elif excedeu_saques:
            print("\033[31m Operação falhou! Número máximo de saques excedido.\033[m")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("\033[31m Operação falhou! O valor informado é inválido.\033[m")

    elif opcao == "e":
        msg = "EXTRATO"
        msg2="="
        print(msg.center(42,"="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(msg2.center(43,"="))
        if saldo < 100:
            print(f"Voce só tem R$ {saldo:.2f}, Voce esta pobre.")
        elif saldo <= 100 or saldo < 200:
                print(f"Você tem R$ {saldo:.2f}, Uau em ! Ja pode ser pobre premium!")
        elif saldo >= 201 or saldo == 300 :
                print(f"Você tem R$ {saldo:.2f}, Parabens agora voce foi promovido a PPP (Pobre Premium Plus)")
        elif saldo >= 301 or saldo == 399:
             print(f"Você tem R$ {saldo:.2f}, Que isso em Papai! Jogo do Tigrinho ta rendendo mesmo!")
        elif saldo >= 400:
             print(f"Voce depositou R$ {saldo:.2f}, Cara para de sonegar imposto a PM vai te pegar! ")                     

    elif opcao == "q":
        break

    else:
        print('\033[31m Operação inválida, por favor selecione novamente a operação desejada.\033[m')