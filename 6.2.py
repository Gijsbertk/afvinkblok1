
prog = "" #variabele met spatie
maxx = 0 #variabale met waarde 0
bestand = intput(open('Bestandsnaam')) #opent bestand 
for n in bestand: #itereert het aantal regels in bestand
    prog += bestand.readline() #voegt regels toe aan bestand
    maxx += 1 #een wordt toegevoegd bij elke iteratie
    if maxx == 5: #stopt na 5 iteraties
        break #breaked
print (prog) #print de variabale
#auteur Gijsbert Keja
