rondje = int(input('Hoeveel rondjes heeft u gelopen?: '))
total = 0.0
langzaamste = 0
snelste = 999

for tijd in range(rondje):
    rondetijd = float(input('Wat zijn u rondetijden?: '))
    total = total + rondetijd
    if rondetijd > langzaamste:
        langzaamste = rondetijd
    if rondetijd < snelste:
        snelste = rondetijd
    


    
gemiddelde = total / rondje    
print(gemiddelde)
print(snelste)
print(langzaamste)
                    
                   
