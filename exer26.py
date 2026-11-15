velocidade = int(input("Velocidade do carro:    "))

if velocidade <= 80:   
    if velocidade < 0:
        print("Como?")
    else:
        print("Siga em paz.")
elif velocidade > 80 and velocidade < 100:
    print("Multa leve de 50 moedas.")
elif velocidade >= 100:
    print("Multa gravíssima de 200 moedas e carro apreendido!")
