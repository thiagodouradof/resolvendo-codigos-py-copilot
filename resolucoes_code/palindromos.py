# Função para verificar se uma palavra é um palíndromo
def verificar_palindromo(palavra):
    # Remover espaços em branco e converter para minúsculas
    palavra = palavra.replace(" ", "").lower()
    # Inverter a palavra
    palavra_invertida = palavra[::-1]
    
    # Comparar a palavra original com a invertida
    return palavra == palavra_invertida

# Solicitar uma palavra ao usuário
entrada = input("Digite uma palavra: ")

# Verificar se é palíndromo e exibir o resultado
if verificar_palindromo(entrada):
    print(f'"{entrada}" é um palíndromo!')
else:
    print(f'"{entrada}" não é um palíndromo.')
