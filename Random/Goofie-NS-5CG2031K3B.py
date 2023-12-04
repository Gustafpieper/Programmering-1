'''
text = input("Skriv ett heltal: ")
tal = int(text)
if tal >= 0:
    print("Talet är positivt")
else:
    print("Talet är negativt")
'''
'''
text = input("Skriv in näst sista siffran i ditt personnummer: ")
tal = int(text)
if tal % 2 == 0:
    print("Du är tjej")
else:
    print("Du är kille")
print("klart")
'''
'''
textett = input("Skriv in ett tal: ")
talett = int(textett)
texttvå = input("Skriv in ett till tal: ")
taltvå = int(texttvå)
if talett > taltvå:
    print("Första talet är större")
elif taltvå > talett:
    print("Andra talet är större")
elif talett == taltvå:
    print("De är lika stora")
'''
'''
text = input("Skriv ett tal: ")
tal = int(text)
if tal > 0 and tal < 10:
    print("Talet är ensiffrigt")
elif tal >= 10 and tal < 100:
    print("Talet är tvåsiffrigt")
elif tal >=100 and tal < 1000:
    print("Talet är tresiffrigt")
elif tal >= 1000:
    print("Talet är minst fyrasiffrigt")
'''

