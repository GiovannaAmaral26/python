def media_coordenadas(coordenadas): 

    soma_x = sum(x for x, y in coordenadas)  

    soma_y = sum(y for x, y in coordenadas) 

    n = len(coordenadas)  

    return (soma_x / n, soma_y / n) 
coordenadas = [(2, 4), (6, 8), (4, 4)] 

media = media_coordenadas(coordenadas) 

print("Média de x e y:", media) 