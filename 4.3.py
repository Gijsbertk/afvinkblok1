rondje = int(input('Hoeveel rondjes heeft u gelopen?: ')) #vraagt om het aantal rodnjes
total = 0.0 #variabele voor later
langzaamste = 0 #variabele voor later
snelste = 999 #variabele voor later

for tijd in range(rondje): #itereert aantal keer het rondje
    rondetijd = float(input('Wat zijn u rondetijden?: ')) #vraagt om de rondetijd aantal keer de iteraties 
    total = total + rondetijd #berekent de totale rondetijd
    if rondetijd > langzaamste: #berekent de langzaamst
        langzaamste = rondetijd #geeft de snelste een variabal
    if rondetijd < snelste: #geeft de snelste een variabale
        snelste = rondetijd #berekent de langzaamst
    


    
gemiddelde = total / rondje   #berekent het gemiddelde 
print(gemiddelde) #print het gemiddelde
print(snelste) #print het snelste
print(langzaamste) #print het langzaamste
                    
                   
