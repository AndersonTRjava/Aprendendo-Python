# Digite um número e fale se é par ou impar
n1 = int(input("Digite um número: "))
if n1 % 2 == 0:
    print(f"O número {n1} é par !")
else:
    print(f"O número {n1} é impar !")

print("")
print("=" * 55)

# Calculando valor de viagem por KM: Até 200km 0,50 por km, maior que isso 0,45 por km

viagem = int(input("Digite a distância da viagem em KM: "))
if viagem <= 200:
    print(f"Você deverá pagar R${round(viagem * 0.50),2}")
else:
    print(f"Você deverá pagar R${round(viagem * 0.45),2}")