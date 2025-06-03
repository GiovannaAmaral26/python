valores = []
while True:
    entrada = int(input("Informe um número inteiro (0 para encerrar): "))
    if entrada == 0:
        break

    colocado = False
    for i in range(len(valores)):
        if valores[i] >= entrada:
            valores.insert(i, entrada)
            colocado = True
            break
    if not colocado:
        valores.append(entrada)

print("Resultado da lista:", valores)
