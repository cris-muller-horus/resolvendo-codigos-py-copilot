# Recebe a palavra do usuário
palavra = input()

# Inverte a palavra
palavra_invertida = palavra[::-1]

# Verifica se é um palíndromo
if palavra == palavra_invertida:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")