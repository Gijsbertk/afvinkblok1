import random #importeert library

nummers = [] #variabele met lege list
for x in range(7): #7 iteraties
    ran_dom = random.randrange(0, 10) # itereert 
    nummers.append(ran_dom) #maakt nieuwe nummers
print(nummers) # print variabele 

ticket = "" #variabele met een spatie
for y in nummers: #itereert de variabele
    ticket += str (x) #voegt per iteratie regel toe
print (ticket)#print variabele
