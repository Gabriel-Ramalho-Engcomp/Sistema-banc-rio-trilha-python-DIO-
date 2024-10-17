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
       valor_deposisto = float(input("Informe o valor que deseja depositar: "))

       if valor_deposisto > 0:
           saldo += valor_deposisto
           extrato += f"Deposito: R${valor_deposisto:.2f}\n"
           print("Deposito realizado com sucesso.")
       else:
           print("Valor inserido invalido.") 
      
    elif opcao == "s":

        if numero_saques >= LIMITE_SAQUES:
            print("Voce atingiu o limite de saques diarios")
        else:
            valor_saque = float(input("Informe o valor que deseja sacar:"))
            if valor_saque > limite:
                print(f"O Valor iserido suepra o limite de R${limite:.2f} por saque")
            elif valor_saque > saldo:
                print("Voce não possui limite suficiente para saque")
            elif valor_saque > 0:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso")
            else:
                print("Operação não concluida, valor informado e invalido.")


    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")