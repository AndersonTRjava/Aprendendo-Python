# Tudo maiúsculo e depois tudo minúsculo, quantas letras sem considerar espaço e quantas letras tem no primeiro nome
nome = str(input("Digite seu nome completo: "))
print(nome.upper())
print(nome.lower())
print(len(nome) - (nome.count(" ")))
dividir = nome.split()
print(len(dividir[0]))

print(" ")

# Mostrar unidade, dezena, centena e milhar
n1 = int(input("Digite um número de 0 a 9999: "))
n2 = str(n1 + 10000)
print(f"Analisando o número: {n1}...\nUnidade: {n2[4]}\n"
      f"Dezena: {n2[3]}\nCentena: {n2[2]}\nMilhar: {n2[1]}")