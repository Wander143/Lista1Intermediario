mesada = float(input("Quanto ganhou de mesada?    "))

preco = float(input("Qual o preço do seu jogo favorito?   "))

if mesada > preco:
    print(f"Aqui o jogo, e o seu troco de {mesada - preco}")
elif mesada == preco:
    print("Aqui o jogo!")
else:
    print(f"Faltam {preco - mesada} para conseguir pagar.")