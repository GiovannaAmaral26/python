dado = input("Informe um valor inteiro: ")
try:
    inteiro = int(dado)
    print(f"Valor convertido com sucesso: {inteiro}")
except ValueError:
    print("Entrada inválida! Não é um número inteiro.")
