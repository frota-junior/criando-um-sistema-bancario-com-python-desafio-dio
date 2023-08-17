
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
        valor = float(input("Por favor, informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")

        else:
            print("\n=== A operação falhou! O valor informado é inválido! ===")

    elif opcao == "s":
        valor = float(input("Por favor, informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\n=== A operação falhou! Você não tem saldo suficiente na sua conta. ===")

        elif excedeu_limite:
            print("\n=== A operação falhou! O valor do saque excedeu o limite permitido. ===")

        elif excedeu_saques:
            print("\n=== A operação falhou! O número máximo diário de saques foi atingido. ===")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")

        else:
            print("\n=== A operação falhou! O número informado é inválido! ===")

    elif opcao == "e":
        
        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=======================================")

    elif opcao == "q":
        break

    else:
        print("\n=== Operação inválida! Por favor, selecione novamente a operação desejada. ===")