def potencias_de_2(expoente_maximo): 

 return [2 ** i for i in range(expoente_maximo + 1)] 

exp = int(input("Digite o expoente máximo: "))  

resultado = potencias_de_2(exp) 

print("Potências de 2 até 2^{}:".format(exp), resultado) 