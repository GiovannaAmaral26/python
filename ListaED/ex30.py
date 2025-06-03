def comprimento_strings(tupla_strings):  

    return tuple(len(s) for s in tupla_strings) 

strings = ("Academia", "Jogos", "Giovanna") 

comprimentos = comprimento_strings(strings) 

print("Comprimentos das strings:", comprimentos) 