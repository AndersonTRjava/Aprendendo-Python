a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
if a == b and a == c:
    print("Os valores são iguais")
else:
    lista = [a, b, c]
    lista.sort()
    print(f"O maior número é: {lista[2]}\nO menor número é: {lista[0]}")