import random #importeert library
print('Je doet steen papier schaar, voor steen kies je 1 voor papier 2 en schaar 3') #print wat je moet doen


def main():
    game() #roept functie aan



def game(): #functie
    speler = int(input('Kies een nummer voor steen papier schaar: ')) #vraagt om functie
    comp = random.randint(1, 3) # random getal wordt toegekend aan variabele
    print(comp) #print varaiabele

    while speler == comp: # als variabele gelijk is aan input
        speler = int(input('Kies een nummer voor steen papier schaar: ')) #opnieuw
        comp = random.randint(1, 3) # opnieuw
        
    
    

                 
    




main()
#auteur gijsbert ekja
