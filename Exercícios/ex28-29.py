# Máquina pensar em um número e tentar acertar qual número ela sorteou
import random
from time import sleep #Faz o computador "pensar"

n1 = random.randint(0, 5) #Faz o computador pensar#
n2 = int(input("Escolha um número inteiro entre 0 e 5: "))
print("Estou pensando...")
sleep(2)
if n2 == n1:
    print("Você Acertou !")
else:
    print(f"Você Errou, o número sorteado foi {n1}")
print(" ")
print("="*70)
print(" ")

# Multar acima de 80km/h R$7,00 por Km/h acima
velocidade = int(input("Digite a velocidade: "))
if velocidade >80:
    print(f" Velocidade da via 80Km/h\n Você passou a {velocidade}Km/h, acima da velocidade permitida !\n"
          f" Deverá Pagar uma multa de R${(velocidade - 80) * 7}")
else:
    print("Dentro da Velocidade Permitida")
