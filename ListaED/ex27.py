def elementos_comuns(lista1, lista2): return list(set(lista1) & set(lista2)) 

lista1 = [1, 2, 3, 4, 5] 

lista2 = [3, 4, 5, 6, 7] 

comuns = elementos_comuns(lista1, lista2)  

print("Elementos comuns:", comuns) 