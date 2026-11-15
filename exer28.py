ano = int(input("Digite um ano: "))

if ano < 1500:
    print("Você encontrou dinossauros ou cavaleiros")
elif ano >= 1500 and ano < 2000:
    print("Você está no século passado")
elif ano == 2026:
    print("Está no ano presente")
else:
    print("Você está no futuro, com carros voadores!")

    