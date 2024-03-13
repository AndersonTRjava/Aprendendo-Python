# Conversão de graus

n1 = int(input("Informe a temperatura em °C: "))
calc = (n1/5)*9+32
print(f" O resultado da Conversão de {n1}°C para Fahrenheit é: {calc}°F")

print("")

# Calculando valor do carro alugado

b1 = int(input("Informe quantos dias ficou com o carro: "))
b2 = str(input("Informe quantos KM percorridos: "))
b2 = b2.replace(",", ".")
b3 = float(b2)
calc2 = (b1*60)+b3*0.15
print(f"Valor total é: R${round(calc2, 2)}")


