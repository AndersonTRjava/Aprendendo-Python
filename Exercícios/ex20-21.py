#Sorteando ordem de alunos
import random
print("Iremos sortear a ordem de alunos\nSerá solicitado que "
      "digite os nomes de cada um.")
print("")
lista = [input("Digite o nome do 1° Aluno: "), input("Digite o nome do 2° Aluno: "),
         input("Digite o nome do 3° Aluno: "), input("Digite o nome do 4° Aluno: ")]
random.shuffle(lista)
print("")
print(f"A ordem sorteada foi: {lista}")

#Carregando uma música
import pygame
pygame.init()
pygame.mixer.music.load("hino-corinthians.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()