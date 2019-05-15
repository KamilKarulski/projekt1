import random

###listy zagniezdzone kolejnosc: pytanie, 4 odpowiedzi, literka poprawnego pytania
###zestawdo pytań 1-4(latwe)
zestaw_pytan_1 = [['Przydomek wiedźmina Geralta wskazuje na to, że bohater sagi Andrzeja Sapkowskiego pochodzi z..','A:Vengerbergu','B:Rivii','C:Oxenfurtu','D:Tretogoru','B'],
['Jaką cześć liter w wyrazie "bajzel" stanowią samogłoski?','A:jedną piątą',' B:jedną trzecią','C:jedną czwartą','D:jedną drugą','B'],
['Na akrod można','A:spać','B:spiewać','C:podróżować','D:pracować','D']]
###zestaw do pytań 5-8(srednie)
zestaw_pytan_2 = []
###zestaw do pytań 9-12(trudne)
zestaw_pytan_3 = []
###lista kolejych wygranych
lista_wygrane = ['500','1 000','2 000','5 000','10 000','20 000','40 000','75 000','125 000','250 000','500 000','1 000 000']

ilosc_pytan = 0
while True:
    if ilosc_pytan < 4:
        wylosowane_pytanie = random.choice(zestaw_pytan_1) #dopóki gracz nie odpowiedział poprawie na 4 pierwsze pytania losuje z pierwszego zestawu
        zestaw_pytan_1.remove(wylosowane_pytanie)
    elif ilosc_pytan >= 4:
        wylosowane_pytanie = random.choice(zestaw_pytan_2) #kiedy gracz odpowiedział poprawie na 4 pierwsze pytania losuje z drugiegoo zestawu
    elif  ilosc_pytan >= 8:
        wylosowane_pytanie = random.choice(zestaw_pytan_3)
    elif ilosc_pytan == 12:
        print("Gratuluje wygrałes milion... bla bla") #12 pytan za nami wiec wygranko xd
    print('Czytam pytanie')
    print(wylosowane_pytanie[0]) #numer listy zagnieżdzonej wybrany, 1 element ponieważ chcemy wyświetlić tylko pytanie
    print(wylosowane_pytanie[1],wylosowane_pytanie[2],wylosowane_pytanie[3],wylosowane_pytanie[4]) #teraz wyswietlamy odpowiedzi
    wygrana = lista_wygrane[0] # pierwszy element w liscie z sianem xd
    print('jaka jest odpowiedz?')
    odpowiedz = input()
    odpowiedz1 = odpowiedz.capitalize() #gdyby gracz wpisał mała a nie duża litere to na wszelki wypadek ją powieksza
    if odpowiedz1 == wylosowane_pytanie[5]: #jeśli odp jest taka sama jak ostatni element listy(czyli poprawna odp)
        print('To poprawna odpowiedz! Twoja wygrana to',wygrana,'zl')
        lista_wygrane.remove(wygrana) #usuwamy z listy z sianem pierwszy element, aby nastepnym razem pokazywalo kolejna wygraną
        ilosc_pytan = ilosc_pytan+1 #dodaje jeden aby python wiedzial ze juz na jedno pytanie byla udzieelona odp, kiedy dojdzie do 4 a potem do 8 bd losowalo z kolejnych list
        print('Oto kolejne pytanie') #petla leci od poczatku
    else:
        break
