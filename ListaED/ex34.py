def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

termo = int(input("Digite qual termo da sequência de Fibonacci deseja ver: "))
resultado = fibonacci(termo)

print(f"O {termo}º termo da sequência de Fibonacci é: {resultado}")
