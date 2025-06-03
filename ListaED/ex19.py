try:   
    a = float(input("Digite o numerador: ")) 
    b = float(input("Digite o denominador: ")) 

    resultado = a / b  
    print("Resultado da divisão:", resultado) 
except ZeroDivisionError:  
    print("Erro: divisão por zero não é permitida.") 