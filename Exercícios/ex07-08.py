# Digite duas notas e calcule a média
s1 = float(input("Digite a nota do primeiro semestre: "))
s2 = float(input("Digite a nota do segundo semestre: "))
media = (s1+s2) / 2
print(f"A média dos dois semestre foi: {round(media, 2)}")

print("")

# Converter um valor para centímetros e milímetros
n = int(input("Digite um valor em metros: "))
print(f"O valor digitado em centímetros é: {n*100}cm \nO valor digitado em milímetros é: {n*1000}mm")