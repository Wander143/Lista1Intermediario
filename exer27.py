nota1 = float(input("Nota da primeira prova (0 a 10): "))
nota2 = float(input("Nota da segunda prova (0 a 10): "))

media = (nota1 + nota2) / 2

print(media)

if media >= 7:
    print("Aprovado")
elif media >= 5 and media < 7:
    print("Recuperação")
elif media < 5:
    print("Reprovado")