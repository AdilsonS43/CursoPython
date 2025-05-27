primeiraNota = float(input("Primeira nota: "))
segundaNota = float(input("Segunda nota: "))
media = (primeiraNota + segundaNota) / 2

print(f"A Média entre {primeiraNota} e {segundaNota} é igual a: {media:.2f} ")

if media < 5:
    print("ALUNO REPROVADO")
elif media < 7:
    print("ALUNO DE RECUPERAÇÃO")
else:
    print("ALUNO APROVADO")
