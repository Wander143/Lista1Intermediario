idade = int(input("Qual sua idade?  "))

animal = int(input("Prefere:\n Gatos(1)\n Cachorros(2)\n"))

if idade < 18:
    if animal == 1:
        print("Jovem e prefere gatos.")
    elif animal == 2:
        print("Jovem e prefere cachorros.")
    else:
        print("Jovem mas animal não foi selecionado corretamente.")
elif idade >= 18:
    if animal == 1:
        print("Adulto e prefere gatos.")
    elif animal == 2:
        print("Adulto e prefere cachorros.")
    else:
        print("Adulto mas animal não foi selecionado corretamente.")