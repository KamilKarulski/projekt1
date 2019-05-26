### milionerzy
import time
import random

ilosc_kol = 3
prawdopodobien = random.random()
p = round(prawdopodobien,2)

kolo_ratunkowe1 = '1: telefon do przyjaciela '
telefon_przyjaciela = 'witaj! tu hubert urbanski z milionerow,\ntwoj przyjaciel gra o milion i potrzebuje twojej pomocy przy pytaniu\nczesc! mam do dyspozycji 4 odp, wskaż swój wybór i powiedz na ile jesteś jej pewny\nhej! mysle, że poprawna jest odp d, chociaż procentowo to raczej tak'
kolo_ratunkowe2 = '2: publicznosc '
glosowanie_publicznosci = 'a więc prosze glosowac\noto wyniki procentowe kolejno dla odp a, b, c i d:\n'
kolo_ratunkowe3 = '3: pol na pol '
pol_na_pol = 'a wiec prosze o odrzucenie 2 blednych odpowiedzi\ndo wyboru pozostały: b i'

prowadzący = ['hm, już wiesz jaka bedzie odp?',  'dobrze ci idzie', 'jak sie czujesz, pewnie wspaniale', 'nie mogę pomóc, takie zasady',
'pamiętaj dużo pieniędzy jest do wygrania', 'na pewno znasz odp na to pytanie',  'co zrobisz jak wygrasz', 'czas na przerwe',
'zapraszam na krótka przerwe','wow!' ]
 ###jego komentarze

czy_chce_kolo_ratunkowe = 'jesli chcesz skorzystac z kola wcisnij "q", jeśli nie to dowolną literę '

print('Witaj w grze MILIONERZY!')
print()
print('czytam zasady gry:\nw grze sa zawsze 4 odp a, b, c, d,\nmasz też do dyspozycji 3 kola ratunlkowe:\n',kolo_ratunkowe1,', ',kolo_ratunkowe2,', ', kolo_ratunkowe3)
print(colored('          0\              o   O   o            -------  ','green'))
print(colored('           ))            /|\ /|\ /|\         ( 50 : 50 )','green'))
print(colored('          0/                 / \               -------  ','green'))
print('Tak przedstawają sie kolejne progi wygranych. Sumy gwarantowane to 1000zł oraz 40 000zł!')
print('-'*szerokosc)
print(colored('| 12    1 000 000zł |','magenta'))
print('| 11      500 000zł |')
print('| 10      250 000zł |')
print('|  9      125 000zł |')
print('|  8       75 000zł |')
print(colored('|  7       40 000zł |','blue'))
print('|  6       20 000zł |')
print('|  5       10 000zł |')
print('|  4        5 000zł |')
print('|  3        2 000zł |')
print(colored('|  2        1 000zł |','blue'))
print('|  1          500zł |')
print('-'*szerokosc)
print('gotowy/gotowa?\nzaczynajmy, gramy o milion zlotych!')
print()


print(random.choice(prowadzący))
print()
print(random.choice(prowadzący))

print(czy_chce_kolo_ratunkowe)
print()
odp_na_kolo_ratunkowe = str(input())
if odp_na_kolo_ratunkowe == 'q':
    print('OK, ktore kolo wybierasz? ', kolo_ratunkowe1, kolo_ratunkowe2,'czy ', kolo_ratunkowe3, '\nwciśnij odpowiednią cyfrę')
    ktore_kolo = str(input())
    if ktore_kolo == '1':
        print('wiec dzwonimy do twojego przyjaciela')
        print(telefon_przyjaciela, p*100)
    elif ktore_kolo == '2':
        print('poprosimy o pomoc publicznosc')

        p1 = random.randint(0,50)
        p2 = random.randint(0,50)
        p3 = random.randint(0,50)
        p4 = random.randint(0,50)
        print(glosowanie_publicznosci, p1, p2, p3, p4)
    elif ktore_kolo == '3':
        po_odrzuceniu1 = random.choice(mozliwe_odp)
        print(pol_na_pol, po_odrzuceniu1)
        print()
    ilosc_kol -= 1
    print('pamietaj, że teraz ilośc twoich kół to:', ilosc_kol)





###listy zagniezdzone kolejnosc: pytanie, 4 odpowiedzi, literka poprawnego pytania
###zestawdo pytań 1-4(latwe)
zestaw_pytan_1 = [['Przydomek wiedźmina Geralta wskazuje na to, że bohater sagi Andrzeja Sapkowskiego pochodzi z..','A:Vengerbergu','B:Rivii','C:Oxenfurtu','D:Tretogoru','B'],
['Jaką cześć liter w wyrazie "bajzel" stanowią samogłoski?','A:jedną piątą',' B:jedną trzecią','C:jedną czwartą','D:jedną drugą','B'],
['Na akrod można','A:spać','B:spiewać','C:podróżować','D:pracować','D'],
['Gromada gadów to inaczej: ', 'A: Arachnida', 'B: Reptilia', 'C: Amphibia', 'D: Insecta', 'B']]
###zestaw do pytań 5-8(srednie)
zestaw_pytan_2 = [['W którym z miast znajdują się korty Flushing Meadows?', 'A: w Londynie', 'B: w Paryżu', 'C: w Nowym Jorku', 'D: w Wiedniu', 'C'],
['Co jest głównym składnikiem maści ichtiolowej?', 'A: tlenek cynku', 'B: szkielet ryb karpiowatych', 'C: łupki bitumiczne','D: tran', 'C'],
['Na strychu suszy się 13 par białych i 9 par czarnych skarpetek. Jest tam tak ciemno, że nie widać ich kolorów. Ile pojedynczych skarpetek powinno się wziąć, by być pewnym, że dwie będą w tym samym kolorze?', 'A:5', 'B:13', 'C:3', 'D:14', 'C'],
['Który aktor urodził się w roku opatentowania kinematografu braci Lumière?', 'A: Rudolph Valentino', 'B: Humphrey Bogart', 'C: Charlie Chaplin', 'D: Fred Astaire', 'A'],
['Kto był pierwszym królem Zjednoczonych Włoch?', 'A:Fryderyk II', 'B:Karol V', 'C:Mikołaj I', 'D:Wiktor Emanuel II', 'D']]
###zestaw do pytań 9-12(trudne)
zestaw_pytan_3 = [['Magazyn "Time" ogłosił w lipcu 2015 r. ranking 10 najbogatszych osób w historii powszechnej. Kto z nich znalazł się najwyżej?', 'A: cesarz Shenzong (Chiny,XI w.)', 'B: Czyngis-chan (Mongolia,XII w.)', 'C: Bill Gates (USA,XX/XXI w.)', 'D: Oktawian August (Rzym, I w. n.e.)', 'D'],
['Yeren to: ', 'A: Bohater jednej z bajek w stylu anime', 'B: Tradycyjna walijska potrawa', 'C: Chiński odpowiednik Wielkiej Stopy', 'D: Imię żony Kim Dzong Una', 'C'],
['System kanałów na rzece Huang He zaplanował i zlecił wykonanie:', 'A: Mao Zedong', 'B: Yu', 'C: Vladimir Putin', 'D: Marco Polo', 'B'],
['Z którym państwem Wielka Brytania toczyła konflikt zbrony o Falklandy w 1982r.?', 'A: z Chile', 'B: z Kolumbią', 'C: z Argentyną', 'D: z Brazylią', 'C'],
['Bouillabaisse to potrawa, z której słynie:', 'A: Bordeaux', 'B: Genua', 'C: Wenecja', 'D: Marsylia', 'D']]
###lista kolejych wygranych
lista_wygrane = ['500','1 000','2 000','5 000','10 000','20 000','40 000','75 000','125 000','250 000','500 000','1 000 000']

ilosc_pytan = 0 #ilość pytań na które gracz do tej pory odpowiedzial, na poczatku musi byc 0
while True:
    if ilosc_pytan < 4:
        wylosowane_pytanie = random.choice(zestaw_pytan_1) #dopóki gracz nie odpowiedział poprawie na 4 pierwsze pytania losuje z pierwszego zestawu
        zestaw_pytan_1.remove(wylosowane_pytanie)
    elif ilosc_pytan >= 4 and ilosc_pytan < 8:
        wylosowane_pytanie = random.choice(zestaw_pytan_2) #kiedy gracz odpowiedział poprawie na 4 pierwsze pytania losuje z drugiegoo zestawu
        zestaw_pytan_2.remove(wylosowane_pytanie)
    elif  ilosc_pytan >= 8 and ilosc_pytan < 13:
        wylosowane_pytanie = random.choice(zestaw_pytan_3)
        zestaw_pytan_3.remove(wylosowane_pytanie)
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
