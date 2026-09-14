total = 0 

for dia in range(1, 8):
    vendas = float(input(f"Digite o valor das vendas do dia {dia} R$: "))
    total += vendas
    
print(f"Faturamneto da semana: R$ {total:.2f}")
