gastos = []

categorias = int(input("Informe a quantidade de categorias de gastos: "))

for i in range(1, categorias + 1):
    valor = float(input(f"Informe o valor de gastos na categoria {i}° (R$):"))
    gastos.append(valor)

total_de_gastos = sum(gastos)

print(f"\nGastos: {gastos}")
print(f"Total de gastos mensais: R$ {total_de_gastos:.2f}")