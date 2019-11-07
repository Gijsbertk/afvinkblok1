def main(): 
    aantal_woorden = vraag() #roept fucntie aan en returned bestand
    verwerk(aantal_woorden) #verwerkt return en roept bestand aan


def verwerk(aantal_woorden): #functie en verwerkt return
    bestand = open('woorden.txt', 'a') #open/creert nieuw bestand
    for x in range(aantal_woorden): # itereety met varaiable
        woord = input('voer je woord in: ') #itereert de var 
        bestand.write(str(woord) + '\n') #itereert de var
    bestand.close() # sluit bestand 
        


def vraag(): #functie
    aantal_woorden = int(input('Hoeveel woorden wil je invoeren?: ')) #vraagt input voor aantal woornden
    return aantal_woorden #returned variabele




main()
#auteur gijsbert keja
