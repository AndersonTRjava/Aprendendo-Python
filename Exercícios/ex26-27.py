# Quantas vezes aparecem a Letra A, em qual posição aparece 1° e qual a última vez em que aparece

n1 = str(input("Digite uma frase: ")).lower().strip().replace("à", "a")\
      .replace("á", "a").replace("ã", "a").replace("â", "a")
print(n1.count("a"))
print(n1.find("a")+1)
print(n1.rfind("a"))

print(" ")

# Selecionar o primeiro e último nome
nome = str(input("Digite seu nome completo: ")).split()
print(f"Seu primeiro nome é: {nome[0]}\n"
      f"Seu último nome é: {nome[len(nome)-1]}")