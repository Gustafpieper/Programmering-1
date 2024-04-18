import random 

kortlek = []
färger = ["spader", "hjärter", "klöver", "ruter"]
valörer = ["2","3","4","5","6","7","8","9","10","knekt","dam","kung","ess"]

for färg in färger:
    for valör in valörer:
        kortlek.append([färg, valör])

random.shuffle(kortlek)

kort = kortlek.pop()
print(kort)




