getal = int(input('Welk getal heeft u op de roulette? ')) #vraagt gebruiker om het getal
if getal == 0: #als getal is 0 print getal is groen
    print('het i groen')

elif getal in (1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36): #als getal is een van de volgende getallen print rood
    print('Het getal',getal,'is rood')
elif getal in (2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35): #als getal is een van de volgende getallen print roodv
    print('Het getal',getal,'is zwart')
