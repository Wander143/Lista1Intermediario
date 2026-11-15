senha = input("Qual a senha:    ")

if senha == "wander":
    print("Correto!")
elif senha == "WANDER":
    print("Quase, mas você gritou a senha (Caps Lock). Tente minúsculas.")
else:
    print("errado")