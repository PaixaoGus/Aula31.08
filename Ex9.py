livros = []

for i in range (3):
    titulos = input(f"Digite o título do {i + 1}° livos: ")
    livros.append(titulos)

print("livros cadastrados:") 

for livro in livros:
    print(livro)
    