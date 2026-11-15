print(f" * (1)Poção de cura: 22 moedas \n * (2)Poção de força: 34 moedas \n * (3)Poção de velocidade: 45 moedas \n ")

moedas = int(input("Quantas moedas tem? "))

escolha = int(input("Digite a poção que deseja (1/2/3)   "))

if escolha == 1:

    if moedas >= 22:
        print(f"Compra efetuada, você tem {moedas - 22} moedas restantes.")
    else:
        print("Moedas insuficientes!")     

elif escolha == 2:

    if moedas >= 34:
        print(f"Compra efetuada, você tem {moedas - 34} moedas restantes.")
    else:
        print("Moedas insuficientes!")

elif escolha == 3:

    if moedas >= 45:
        print(f"Compra efetuada, você tem {moedas - 45} moedas restantes.")
    else:
        print("Moedas insuficientes!") 
else:
    print("ERRO: Nenhuma escola com esse valor.")
