#aumento sucessivo de salário.
salario = str(input("Digite o valor do seu Salário: R$ "))

salario = salario.replace(",",".")

salario1 = float(salario)

if salario1 <= 1250:
    aumento = (salario1 * 0.15) + salario1

else:
    aumento =(salario1 * 0.10) + salario1

print(f"O seu salário de R${salario1:.2f} foi para R${aumento:.2f}")

print("")
print("-="*30)
print("")

#formação de um triângulo

import time
l1 = float(input("Digite o valor do primeira lado: "))
l2 = float(input("Digite o valor do primeira lado: "))
l3 = float(input("Digite o valor do primeira lado: "))

print("Calculando o aumento...")
time.sleep(2)
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print("Esses valores FORMAM um triângulo")
else:
    print("Esses valores NÃO formam um triângulo")