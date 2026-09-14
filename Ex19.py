numero = int(input("Digite um valor inteiro positivo: "))

fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print(f"O fatorial de {numero} e: {fatorial}")