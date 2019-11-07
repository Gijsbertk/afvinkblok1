nummers = [] #lege list 
for vragen in range(20): # 20 iteraties
     B = input ("voer 20 nummers in") # itereert
     nummers.append(B) # schrijft elke eer bij 
gem = 0  #variabele met waarde 0
get = 0 #variabele met waarde 0
laagste = nummers[0] #variabele wordt nummer in list aangeroepen
hoogste = nummers[0] #variabele wordt nummer in list aangeroepen
for y in nummers: #itereert de aantal nummers
    gemiddeld += int (y) #voegt na de aantal ieteraties waarde toe aan var
    get += int (y) #voegt na de aantal ieteraties waarde toe aan var
    if int (laagste) > int (y): #if staement met gorter dan variabele
        laagste = y #laagste krijgt een nieuwe waarde
    elif int (hoogste) < int (y): #if staement met kleiner dan variabele
        hoogste = y #hoogste krijgt een nieuwe waarde
gemiddeld = gemiddeld / len(nummers) #berkent gemiddlede
print (gemiddeld) #print var
print (get) #print var
print ("laagste " + laagste) #print var 
print ("hoogste " + laagste) #print var
#auteur gijsbert keja
