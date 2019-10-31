import random
print('Je doet steen papier schaar, voor steen kies je 1 voor papier 2 en schaar 3')


def main():
    game()



def game():
    speler = int(input('Kies een nummer voor steen papier schaar: '))
    comp = random.randint(1, 3)
    print(comp)

    while speler == comp:
        speler = int(input('Kies een nummer voor steen papier schaar: '))
        comp = random.randint(1, 3)
        
    
    

                 
    




main()
