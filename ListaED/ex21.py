def abrir_arquivo():
    try:
        nome_arquivo = input("Digite o nome do arquivo : ")
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo:")
            print(conteudo)
    except FileNotFoundError:
        print("Erro: o arquivo não pode ser encontrado.")
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")

abrir_arquivo()