def numeros_pares(n): 

 return list(range(0, n + 1, 2)) 

n = int(input("Digite o valor de N: ")) 
pares = numeros_pares(n) 

print("Números pares de 0 até", n, ":", pares) 