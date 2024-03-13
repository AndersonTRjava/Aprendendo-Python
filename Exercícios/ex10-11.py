# Conversão cambial

n = str(input("Qual o valor que precisa em dólares: U$"))
n = n.replace(",", ".")
n1 = float(n)
n2 = float(n1 * 4.98)
print(f"Você precisa de R${round(n2, 2)} para obter U${round(n1, 2)}")

print('')
# Calculando total de tinta para pintar parede

larg = float(input("Digite a largura em metros da sua parede: "))
h = float(input("Digite a altura em metros da sua parede: "))
calc = larg * h
print(f"Você irá precisar de {round(calc/2,2)}L de tinta para pintar a parede de {calc}m²")