senha_letras = input("Qual sua senha com letras:    ")


if senha_letras == "wander":
    
    pin = int(input("Qual seu PIN:  "))

    if pin == 1143:
        print("Acesso ao cofre liberado.")
            
    else:
        print("Errado")
        
else:
    print("Errado")