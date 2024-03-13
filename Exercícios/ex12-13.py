# Calculo de desconto
n = str(input("Seja bem-vindo cliente! \nDigite o valor do produto: R$"))
n = n.replace(",", ".")
n1 = float(n)
n2 = str(input("Digite o valor do desconto: "))
n2 = n2.replace("%", "")
n3 = int(n2)
calc = n1-(n3/100)*n1
print(f"O valor final do produto com aplicação do desconto é de: R${round(calc,2)}")

print("")
# Aumento no salário

a = str(input("Digite seu salário: R$"))
a = a.replace(",", ".")
a1 = float(a)
calc2 = a1+(a1 * 0.15)
print(f"O salário de {a1} com aumento de 15% passa a ser de R${round(calc2,2)}")