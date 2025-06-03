def aplicar_funcao(lista, funcao):  

    return [funcao(elemento) for elemento in lista] 

numeros = [2, 4, 6, 8, 10] 
dobro = lambda x: x * 2 

resultado = aplicar_funcao(numeros, dobro)  

print("Resultado após aplicar a função:", resultado) 