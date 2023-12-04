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
'''
text1 = input("skriv ett tal")
text2 = input("skriv ett till tal")
text3 = input("skriv ett sista tal")
tal1 = int(text1)
tal2 = int(text2)
tal3 = int(text3)
if tal1 < tal2 and tal3:
    print(tal1,"är minst")
elif tal2 < tal1 and tal3:
    print(tal2,"är misnt!")
elif tal3 < tal1 and tal2:
    print(tal3,"är minst!")
'''
'''
text1 = input("skriv ett tal")
text2 = input("skriv ett till tal")
text3 = input("skriv ett sista tal")
tal1 = int(text1)
tal2 = int(text2)
tal3 = int(text3)
if tal1 < tal2 < tal3:
    print(tal1, tal2, tal3)
elif tal1 < tal3 < tal2:
    print(tal1, tal3, tal2)
elif tal2 < tal1 < tal3:
    print(tal2, tal1, tal3)
elif tal2 < tal3 < tal1:
    print(tal2, tal3, tal1)
elif tal3 < tal1 < tal2:
    print(tal3, tal1, tal2)
elif tal3 < tal2 < tal1:
    print(tal3, tal2, tal1)
'''

text = input("Skriv in din födelsemånad")
if text == Januari or text == januari or text == Februari or text == februari or text == December or text == december:
    print("Du är född på vintern")
elif text == Mars or text == mars or text == April or text == april or text == Maj or text == maj:
    print("Du är född på våren")
elif text == Juni or text == juni or text == Juli or text == juli or text == Augusti or text == augusti:
    print("Du är född på sommaren")
elif text == September or text == september or text == Oktober or text == oktober or text == November or text == november:
    print("Du är förr på hösten")
    


































