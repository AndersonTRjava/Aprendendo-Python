# Calculando Sen e Cos
from math import radians, cos, sin, tan
n1 = float(input("Digite o valor em ângulo: "))
print(f"O ângulo digitado foi: {n1}°\n"
      f"Seu Cosseno é: {round(cos(radians(n1)), 2)}\n"
      f"Seu Seno é: {round(sin(radians(n1)), 2)}\n"
      f"A Tangente é: {round(tan(radians(n1)), 2)}")

print("")

# Sorteando um aluno
from random import choice
print("Iremos sortear 1 Aluno entre 4.\nSerá solicitado que digite o nome dos alunos\n")

lista = input("Digite o nome do 1° Aluno: "), input("Digite o nome do 2° Aluno: "), \
        input("Digite o nome do 3° Aluno: "), input("Digite o nome do 4° Aluno: ")
print(" ")
print(f"O Aluno sorteado foi o(a): {choice(lista)}")