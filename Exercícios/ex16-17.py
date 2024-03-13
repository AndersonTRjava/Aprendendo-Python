# Arredondando número real

n1 = float(input("Digite um número real: "))
print(round(n1, 0))

import math

# Descobrindo valor da Hipotenusa

c1 = float(input("Digite o valor do cateto adjacente em cm: "))
c2 = float(input("Digite o valor do cateto oposto em cm: "))
calc = (c1 ** 2 + c2 ** 2)
print(f"O valor da hipotenusa é: {round(math.sqrt(calc), 2)}cm")