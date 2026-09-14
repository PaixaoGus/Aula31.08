codigos = [10, 58, 69, 268, 298, 321, 584]

codigo = int(input("Informe o codigo do produto: "))

if codigo in codigos:
    print("O codigo esta na lista.")
else:
    print("O codigo nao esta na lista.")