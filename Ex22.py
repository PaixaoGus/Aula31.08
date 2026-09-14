notas = []

quantidade_de_estudantes = int(input("Informe a quantidade de estudante: "))

for i in range(1, quantidade_de_estudantes + 1):
    nota = float(input(f"informe a nota do estudande {i}: "))
    notas.append(nota)
      
maior_nota = max(notas)

print(f"\nLista de notas cadastradas: {notas}")
print(f"A maior nota registrada foi: {maior_nota:.2f}")

    
