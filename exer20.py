dinheiro = float(input("Quanto de dinheiro tem? "))

escolha = int(input(f"Escolhe o:\n Lanche R$15,00 (1)\n Suco R$8,00 (2)\n Combo R$20,00 (3)\n"))

if escolha == 1:
    if dinheiro >= 15:
        print(f"Compra confirmada, seu troco é de R${dinheiro - 15}")
    else:
        print("Compra negada.")
elif escolha == 2:
    if dinheiro >= 8:
        print(f"Compra confirmada, seu troco é de R${dinheiro - 8}")
    else:
        print("Compra negada.")
elif escolha == 3:
    if dinheiro >= 20:
        print(f"Compra confirmada, seu troco é de R${dinheiro - 20}")
    else:
        print("Compra negada.")
else:
    print("ERRO: Nenhuma escola com esse valor.")