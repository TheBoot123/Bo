def check_raad(raad, antwoord):
    global score
    nog_radend = True
    poging = 0
    while nog_radend and poging < 3:
        if raad.lower() == antwoord.lower():
            print('Correct antwoord')
            score = score + 1
            nog_radend = False
        else:
            if poging < 2:
                raad = input('Sorry verkeerd antwoord. probeer opnieuw. ')
            poging = poging + 1

    if poging == 3:
        print('Het correcte antwoord is ' + antwoord)


score = 0
print('raad het dier')
raad1 = input('Welke beer leeft op de Noordpool? ')
check_raad(raad1, 'ijsbeer')
raad2 = input('wat is het snelste landdier? ')
check_raad(raad2, 'luipaard')
raad3 = input('welke dier lijkt op een dino dat er nu nog is? ')
check_raad(raad3, 'kip')
raad4 = input('welk dier heeft een lange nek? ')
check_raad(raad4, 'girafe')
raad5 = input('wat is het grootste dier in de wereld? ')
check_raad(raad5, 'blauwe vinvis')

print('Quiz 2')

raad = input('Welke hiervan is een vis?\n \
A) Walvis\n B) Dolfijn\n C) Haai\n D) Pijinktvis\n \
Typ A, B, C, D ')
check_raad(raad, 'C')

print('Jouw score is ' + str(score))
