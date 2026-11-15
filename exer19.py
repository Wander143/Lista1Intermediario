mesada = 50

bonus = bool(input("Recebeu nota A em Matemática? (Sim/Não)   ") == "Sim")

if bonus:
    mesada += 20
    print(f"Sua nova mesada é {mesada} com o bônus em matemática!")
else:
    print(f"Sua mesada sera {mesada} então.")