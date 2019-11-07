def main():
    aantal_woorden = vraag()
    verwerk(aantal_woorden)


def verwerk(aantal_woorden):
    bestand = open('woorden.txt', 'a')
    for x in range(aantal_woorden):
        woord = input('voer je woord in: ')
        bestand.write(str(woord) + '\n')
    bestand.close()
        


def vraag():
    aantal_woorden = int(input('Hoeveel woorden wil je invoeren?: '))
    return aantal_woorden




main()
