print("Responda para entrar na Taverna do Dragão!\n")

senha = input("Qual a senha?  ")

if senha == "senhasegura123":
    print("\nVocê passou o primeiro teste!")

    idade = int(input("\nQual sua idade?    "))

    if idade < 13:
        print("\nVocê recebeu um Suco de Uva\n")
    elif idade >= 13:
        print("\nVocê recebeu a Poção Mágica!\n")

    moedas = int(input("Quanto de moedas tem?   "))

    persona = int(input("Você prefere\n 1-Sorvete\n 2-Bolo  \n"))
    
    
    if persona == 1:
        comprar = input("\nVocê gostaria de comprar o Cetro de Gelo? S/N (55 moedas)  ")

        if comprar == "S":
            if moedas >= 55:
                print(f"\nCompra efetuada! Troco: {moedas - 55}")
                print("Você saiu da Taverna com o Cetro de Gelo em mãos")
            else:
                print("\n Desculpe, moedas insuficientes.")
                print("\nVocê saiu da Taverna de mão vazias")
        elif comprar == "N":
                print("\nVocê saiu da Taverna de mão vazias")
        else:
            print("Nenhuma opção encontrada")

    elif persona == 2:
        comprar = input("Você gostaria de comprar o Escudo de Slime? S/N (25 moedas)  ")

        if comprar == "S":
            if moedas >= 25:
                print(f"\nCompra efetuada! Troco: {moedas - 25}")
                print("Você saiu da Taverna com o Escudo de Slime em mãos")
            else:
                print("\n Desculpe, moedas insuficientes.")
                print("\nVocê saiu da Taverna de mão vazias")
        elif comprar == "N":
                print("\nVocê saiu da Taverna de mão vazias")
        else:
            print("Nenhuma opção encontrada")
    else:
        print("Nenhuma opção encontrada")
            
else:
    print("Sua entrada foi negada, volte quando souber a senha!")


