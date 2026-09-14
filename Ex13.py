consumo1 = float(input("Digite o consumo do setor 1: "))
consumo2 = float(input("Digite o consumo do setor 2: "))

if consumo1 > consumo2:
    print("O setor 1 apresentou o maior consumo.")
elif consumo2 > consumo1:
    print("O setor 2 apresentou o maior consumo.")
else:
    print("Os dois setores apresentaram o mesmo consumo.")