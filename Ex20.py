total = 0 

nota = float(input("Digite uma nota (0 para encerrar): "))

while nota != 0:
    total += nota
    nota = float(input("Digite uma nota (0 para encaerrar): "))
    
print("Soma total dos valores digitados:", total)