lijst = [] #lege lijst 

def main(): 
    list_ = b_open() #returned var en roept functie aan 
    gemiddelde(list_) #verwerkt var en ropet functie aan
    hoog(list_) #verwerkt var en ropet functie aan

def b_open():
    bestand = open("SC_expression.csv") #opent bestand
    bestand.readline() # lees regel bestand 
    
    for regel in range(len(bestand)): #itereet over var 
        regel = bestand.readline() #voert uit over iteratie
        regel = regel.strip() #voert uit over iteratie
        regel = regel.split(",") #voert uit over iteratie
        list_.append(regel) #voert uit over iteratie 
    return(list_) # returned var 
	



def hoog(list_):
    kolom = int(input ("Welke kolom wil je hebben?")) # input 
    for getal in range(len(list_)): #itereert over var
        waarde = float (list_[getal][kolom]) #voert uit na iteratie
        if waarde > 50 or waarde == 50: #kijkt of statement true is 
            print (list_[getal][0]) #print de var
        



def gemiddelde(list_):
    kolom = int(input ("Welke kolom wil je hebben?")) #vraagt om input
    gem = 0 #var zonder waarde 
    for getal in range(len(list_)): #itereert over elke waarde 
        gem += float (list_[getal][kolom]) #voert dit bij elke iteratie uit
          
    gem = gem / len(list_) #berekend gemiddled
    print (gem) #print var

main()
