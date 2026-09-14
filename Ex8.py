total_de_alimentos = 0

for voluntarios in range (1, 6):
    quantidade = int(input(f"Digite a quantidade de alimentos arrecadados pelo voluntario {voluntarios} (em Kg): "))
    total_de_alimentos += quantidade
    
print(f"Total de Alimentos arrecadados pelos voluntarios: {total_de_alimentos}Kg")