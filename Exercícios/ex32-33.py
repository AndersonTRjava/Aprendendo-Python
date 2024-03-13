# Digite um ano e diga se ele é BISSEXTO
from datetime import date
ano = int(input("Qual ano quer Analisar? (digite 0 para analisar o ano atual) : "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"{ano} é um ano Bissexto")
else:
    print(f"{ano} não é Bissexto")

# Digite 3 números e mostre qual é o maior e menor
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

# Verificando o menor número
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
# Verificando o maior número
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f"O menor número é o: {menor}\nO maior número é o: {maior}")