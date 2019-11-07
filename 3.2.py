breedte1 = float(input('wat is de breedte van het object1? ')) #vraag gebruiker om breedte object1
lengte1 = float(input('wat is de lengte van het object1? ')) #vraag gebruiker om lengte object1


breedte2 = float(input('wat is de breedte van het object2? ')) #vraag gebruiker om breedte object2
lengte2 = float(input('wat is de lengte van het object2? ')) #vraag gebruiker om lengte object2

if breedte2 * lengte2 == breedte1 * lengte1: #berekent of de oppervlakte even groot
    print('de vierkanten zijn even groot') #als de oppervlakte even groot is print hij de print
elif breedte2 * lengte2 <= breedte1 * lengte1:
    print('de vierkant1 is groter')
elif breedte2 * lengte2 >= breedte1 * lengte1:
    print('de vierkant2 is groter')
#auteur gijsbert keja
