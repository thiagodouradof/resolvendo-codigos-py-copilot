# Solicitar um número inteiro como entrada
numero = int(input("Digite um número inteiro: "))

# Verificar se o número é par ou ímpar
if numero % 2 == 0:
    resultado = "par"
else:
    resultado = "ímpar"

# Exibir o resultado
print(f"O número {numero} é {resultado}.")
