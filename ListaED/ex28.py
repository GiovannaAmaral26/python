def pessoa_mais_velha(lista): 

    return max(lista, key=lambda pessoa: pessoa[1]) 

pessoas = [("Ana Clara", 32), ("Marcelo", 50), ("Sandra", 40)] 

mais_velha = pessoa_mais_velha(pessoas) 

print("Pessoa mais velha:", mais_velha[0], "com", mais_velha[1], "anos") 