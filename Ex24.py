partcipantes = []

quantidade = int(input("Informe a quantidade de participante: "))

for i in range(1, quantidade + 1):
    nome = input(f"Informe o nome do {i}° participante a chegar: ")
    partcipantes.append(nome)
    
partcipantes.reverse()

print(f"\nNome na ordem Inversa:")
print(partcipantes)