import random # importeert library


def main():
    aantal = roll() #returned var en ropet fucntie aan
    verwerk(aantal) #verwerkt var en roept fucntie aan


def verwerk(aantal): #fucntie
    
    lijst = [] #maakt lege lijst
    for x in range(aantal): # itereert var
        nummer = random.randint(1, 6) #willekeurig nummer na iteratie
        lijst.append(nummer) #schijft nieuwe waarde toe aan lijst
    print(lijst) #print var

        






def roll(): #functie
    aantal = int(input('Hoe vaak heb je gegooid?(je kan alleen een positieve invullen): ')) #vraagt om input
    return aantal #returned var




main()
#auteur gijsbert keja
