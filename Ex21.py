produtos = []

for i in range(5):
    produto = input(f"Digite o nome do {i + 1}° protudos: ")
    produtos.append(produto)
    
print("\nLista de Produtos:")
print(produtos)