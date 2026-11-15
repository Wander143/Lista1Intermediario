pergunta = int(input("Prefere atacar:\n De longe(1)\n De perto(2)\n"))

classe = "Não definida"

if pergunta == 1:

    pergunta_longe = str(input(" Magia(A)\n Arco(B)\n"))

    if pergunta_longe == "A":
        classe = "Mago"
    elif pergunta_longe == "B":
        classe = "Arqueiro"
    else:
        print("Opcão não encontrada.")
elif pergunta == 2:

    pergunta_perto = str(input(" Espada(A)\n Adagas(B)\n"))

    if pergunta_perto == "A":
        classe = "Guerreiro"
    elif pergunta_perto == "B":
        classe = "Assassino"
    else:
        print("Opcão não encontrada.")        
else:
    print("Opcão não encontrada.")

print(f"Sua classe é {classe}!")
