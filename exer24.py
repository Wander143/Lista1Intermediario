cor = input("Escolha uma cor:   ")

emocao = "nada"

if cor == "Azul":
    emocao = "Calmo"
elif cor == "Vermelho":
    emocao = "Zangado"
elif cor == "Amarelo":
    emocao = "Alegre"
else:
    emocao = "Única"

print(f"Sua emoção é:{emocao}")
