qtd = int(input("Informe o número de elementos (mínimo 2): "))

if qtd < 2:
    print("Aviso: o valor precisa ser pelo menos 2.")
else:
    serie = [0, 1]
    for i in range(2, qtd):
        novo = serie[i - 1] + serie[i - 2]
        serie.append(novo)

    print("Sequência gerada:", serie)
