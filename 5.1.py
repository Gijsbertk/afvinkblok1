def main():
    kilometer = vraag()
    miles = kilometer * 0.6214
    print('Je hebt',miles,'mijlen afgelegd')
    
        

def vraag():
    kilometer = int(input('Hoeveel kilometer heb je gereden?: '))
    return kilometer




main()
