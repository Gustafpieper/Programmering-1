def celsuistofarenheight(celsius):
    answer = (9/5) * celsius + 32
    return answer
    
svar=float(input("Skriv in en grad: "))
print(celsuistofarenheight(svar), "F")