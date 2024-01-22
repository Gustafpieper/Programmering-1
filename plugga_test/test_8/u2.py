import random

lista = [random.randint(1,6) for _ in range(20)]

antal_treor = lista.count(3)

print(antal_treor)