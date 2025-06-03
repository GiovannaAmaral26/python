texto = input("Digite um valor: ")

try:
    numero = int(texto)
    print("Conversão bem-sucedida! Número inteiro:", numero)
except ValueError:
    print("Erro: não foi possível converter para número inteiro.")
