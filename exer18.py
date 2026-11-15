tesouro = int(input("Qual o valor do seu tesouro:   "))

if tesouro > 1000:

    tesouro *= 0.9

    print(f"Taxa de 10%, novo tesouro é {tesouro}")
    
elif tesouro <= 1000:
    print(f"Sem taxa de 10%, seu tesouro é {tesouro}")