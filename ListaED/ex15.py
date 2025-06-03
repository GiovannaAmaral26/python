saldo = float(input("Digite o saldo da conta: ")) 
valor_saque = float(input("Digite o valor do saque: ")) 

if valor_saque <= saldo:
    saldo -= valor_saque
    print(f"Saque realizado com sucesso! Saldo restante: R$ {saldo:.2f}")
else:
    print("Saldo insuficiente para realizar o saque.")