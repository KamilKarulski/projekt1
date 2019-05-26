### milionerzy
import time
import random
from colorama import init
from termcolor import colored
init()
ilosc_kol = 3
odp=['A','B','C','D']
prawdopodobien2 = random.randint(50,100)
p2=round(prawdopodobien2,2)
szerokosc = 21

kolo_ratunkowe = ['1. Telefon do przyjaciela','2. Pytanie do publiczności','3. 50:50']
czy_chce_kolo_ratunkowe = 'Jeżeli chcesz skorzystać z koła ratunkowego, wciśnij "q" i ENTER. Jeżeli nie, wciśnij ENTER, aby kontynuować. '

###jego komentarze
prowadzacy = ['Dobrze Ci idzie!','Świetnie, oby tak dalej.','W takim tempie zaraz dojdziemy do miliona!','Zdenerwowany?','Walczymy dalej!','Jesteś gotowy na następne pytania?']


print("Witaj w grze")
print()
time.sleep(1)
print(colored("\t$   $  $$$  $     $$$   $$$   $   $  $$$$  $$$$   $$$$$  $   $\n\t$$ $$   $   $      $   $   $  $$  $  $     $   $     $    $ $ \n\t$ $ $   $   $      $   $   $  $ $ $  $$$   $$$$     $      $ \n\t$   $   $   $      $   $   $  $  $$  $     $ $     $       $\n\t$   $  $$$  $$$$  $$$   $$$   $   $  $$$$  $  $$  $$$$$    $","yellow"))
print()
print("Wciśnij ENTER, aby kontynuować.")
kontynuuj = str(input())
print()
print('Przedstawię szybko zasady rozgrywki:')
time.sleep(1)
print('Wszystkie pytania mają 4 możliwe odpowiedzi - A, B, C, D.')
time.sleep(2)
print('W razie zwątpienia, do Twojej dyspozycji są 3 koła ratunkowe:',kolo_ratunkowe[0], kolo_ratunkowe[1], kolo_ratunkowe[2])
print(colored('          0\              o   O   o            -------  ','green'))
print(colored('           ))            /|\ /|\ /|\         ( 50 : 50 )','green'))
print(colored('          0/                 / \               -------  ','green'))
time.sleep(3)
print()
print('W grze istnieją 2 progi kwoty gwarantowanej - 5 000 i 75 000.\nOznacza to tyle, że nawet jeżeli ne dotrzesz do końca rozgrywki, możesz wrócić do domu z pieniędzmi.')
print('-'*szerokosc)
print(colored('| 12    1 000 000zł |','magenta'))
print('| 11      500 000zł |')
print('| 10      250 000zł |')
print('|  9      125 000zł |')
print(colored('|  8       75 000zł |','blue'))
print('|  7       40 000zł |')
print('|  6       20 000zł |')
print('|  5       10 000zł |')
print(colored('|  4        5 000zł |','blue'))
print('|  3        2 000zł |')
print('|  2        1 000zł |')
print('|  1          500zł |')
print('-'*szerokosc)
time.sleep(3)
print()
print('Gotowy/a?\nA więc zaczynajmy! Przypominam: gra toczy się o milion złotych.')
print()
time.sleep(1)
print('Czas na pierwsze pytanie...')



###listy zagniezdzone kolejność: pytanie, 4 odpowiedzi, literka poprawnego pytania
###zestaw do pytań 1-4 (latwe)
zestaw_pytan_1 = [['Przydomek wiedźmina Geralta wskazuje na to, że bohater sagi Andrzeja Sapkowskiego pochodzi z...','A. Vengerbergu','B. Rivii','C. Oxenfurtu','D. Tretogoru','B'],
['Jaką cześć liter w wyrazie "bajzel" stanowią samogłoski?','A. jedną trzecią',' B. jedną piątą','C. jedną czwartą','D. jedną drugą','A'],
['Na akord można:','A. spać','B. śpiewać','C. podróżować','D. pracować','D'],
['Gromada gadów to inaczej: ', 'A. Arachnida', 'B. Reptilia', 'C. Amphibia', 'D. Insecta', 'B']]
###zestaw do pytań 5-8(srednie)
zestaw_pytan_2 = [['W którym z miast znajdują się korty Flushing Meadows?', 'A. w Londynie', 'B. w Paryżu', 'C. w Nowym Jorku', 'D. w Wiedniu', 'C'],
['Co jest głównym składnikiem maści ichtiolowej?', 'A. tlenek cynku', 'B. szkielet ryb karpiowatych', 'C. łupki bitumiczne','D. tran', 'C'],
['Na strychu suszy się 13 par białych i 9 par czarnych skarpetek. Jest tam tak ciemno, że nie widać ich kolorów. Ile pojedynczych skarpetek powinno się wziąć, by być pewnym, że dwie będą w tym samym kolorze?', 'A.5', 'B.13', 'C.3', 'D.14', 'C'],
['Który aktor urodził się w roku opatentowania kinematografu braci Lumière?', 'A. Rudolph Valentino', 'B. Humphrey Bogart', 'C. Charlie Chaplin', 'D. Fred Astaire', 'A'],
['Kto był pierwszym królem Zjednoczonych Włoch?', 'A. Fryderyk II', 'B. Karol V', 'C. Mikołaj I', 'D. Wiktor Emanuel II', 'D']]
###zestaw do pytań 9-12(trudne)
zestaw_pytan_3 = [['Magazyn "Time" ogłosił w lipcu 2015 r. ranking 10 najbogatszych osób w historii powszechnej. Kto z nich znalazł się najwyżej?', 'A. cesarz Shenzong (Chiny,XI w.)', 'B. Czyngis-chan (Mongolia,XII w.)', 'C. Bill Gates (USA,XX/XXI w.)', 'D. Oktawian August (Rzym, I w. n.e.)', 'D'],
['Yeren to: ', 'A. Bohater jednej z bajek w stylu anime', 'B. Tradycyjna walijska potrawa', 'C. Chiński odpowiednik Wielkiej Stopy', 'D. Imię żony Kim Dzong Una', 'C'],
['System kanałów na rzece Huang He zaplanował i zlecił wykonanie:', 'A. Mao Zedong', 'B. Yu', 'C. Vladimir Putin', 'D. Marco Polo', 'B'],
['Z którym państwem Wielka Brytania toczyła konflikt zbrony o Falklandy w 1982r.?', 'A. z Chile', 'B. z Kolumbią', 'C. z Argentyną', 'D. z Brazylią', 'C'],
['Bouillabaisse to potrawa, z której słynie:', 'A. Bordeaux', 'B. Genua', 'C. Wenecja', 'D. Marsylia', 'D']]
###lista kolejych wygranych
lista_wygrane = ['500','1 000','2 000','5 000','10 000','20 000','40 000','75 000','125 000','250 000','500 000','1 000 000']

###kwoty gwarantowane
gwarantowana = ['5 000','75 000']

###lista pytań prowadzacego o odpowiedz
jakaodpowiedz=['Jaka jest odpowiedź?','Która odpowiedź jest poprawna?','Poprawna odpowiedź na to pytanie to...','Jak odpowiesz na to pytanie?','Czy znasz odpowiedź?']

###lista reakcji na poprawną odpowiedź
poprawna=['Dobra odpowiedź! Grasz dalej.','Niestety, jest to...poprawna odpowiedź! Gramy dalej.','Tak, to jest dobra odpowiedź!','Tak, to poprawna odpowiedź!','To jest poprawna odpowiedź!','Świetnie, odpowiedziałeś/aś poprawnie!']

ilosc_pytan = 0 #ilość pytań na które gracz do tej pory odpowiedzial, na poczatku musi byc 0

while True:
    if ilosc_pytan <4:
        wylosowane_pytanie = random.choice(zestaw_pytan_1) #dopóki gracz nie odpowiedział poprawnie na 4 pierwsze pytania losuje z pierwszego zestawu
        zestaw_pytan_1.remove(wylosowane_pytanie)
    elif ilosc_pytan >4 and ilosc_pytan <8:
        wylosowane_pytanie = random.choice(zestaw_pytan_2) #kiedy gracz odpowiedział poprawnie na 4 pierwsze pytania losuje z drugiegoo zestawu
        zestaw_pytan_2.remove(wylosowane_pytanie)
    elif  ilosc_pytan >8 and ilosc_pytan <=12:
        wylosowane_pytanie = random.choice(zestaw_pytan_3)
        zestaw_pytan_3.remove(wylosowane_pytanie)
        if ilosc_pytan == 12:
            print("GRATULACJE!\nWYGRAŁEŚ 1 000 000 ZŁOTYCH!")
            break
    print(wylosowane_pytanie[0]) #numer listy zagnieżdzonej wybrany, 1 element ponieważ chcemy wyświetlić tylko pytanie
    print(wylosowane_pytanie[1],wylosowane_pytanie[2],wylosowane_pytanie[3],wylosowane_pytanie[4]) #teraz wyswietlamy odpowiedzi
    wygrana = lista_wygrane[0] # pierwszy element w liscie z sianem xd
    if len(kolo_ratunkowe)>0:
        print(czy_chce_kolo_ratunkowe)
        odp_na_kolo_ratunkowe = str(input())
        if odp_na_kolo_ratunkowe == 'q':
            print('Zdecydowałeś się na koło ratunkowe. Z którego koła chcesz skorzystać?\nAby wybrać, wciśnij odpowiednią cyfrę.')
            print('Dostępne koła ratunkowe:',kolo_ratunkowe)
            ktore_kolo = str(input())
            if ktore_kolo == '1':
                print('\nDzwonimy do Twojego przyjaciela.')
                print('H: Witaj! Z tej strony Hubert Urbański z Milionerów.\nTwój przyjaciel gra właśnie o milion i potrzebuje Twojej pomocy przy pytaniu.\nMasz do dyspozycji 4 odpowiedzi.\nP: Myślę, że poprawna jest odpowiedź',wylosowane_pytanie[5],'i jestem tego pewny na', p2,'%. Mogę się jednak mylić...\n')
                kolo_ratunkowe.remove('1. Telefon do przyjaciela')
            elif kto   re_kolo == '2':
                print('\nProszę publiczność o zagłosowanie na poprawną państwa zdaniem odpowiedź.\nOto wyniki procentowe kolejno dla odp A, B, C i D:')
                A = random.randint(5,95)
                B = random.randint(5,95)
                C = random.randint(5,95)
                D = random.randint(5,95)
                while (A+B+C+D)!=100:
                    A = random.randint(5,95)
                    B = random.randint(5,95)
                    C = random.randint(5,95)
                    D = random.randint(5,95)
                    if wylosowane_pytanie[5]=='A':
                        while A<=B or A<=C or A<=D:
                            A = random.randint(5,95)
                            B = random.randint(5,95)
                            C = random.randint(5,95)
                            D = random.randint(5,95)
                    elif wylosowane_pytanie[5]=='B':
                        while B<=A or B<=C or B<=D:
                            A = random.randint(5,95)
                            B = random.randint(5,95)
                            C = random.randint(5,95)
                            D = random.randint(5,95)
                    elif wylosowane_pytanie[5]=='C':
                        while C<=B or C<=A or C<=D:
                            A = random.randint(5,95)
                            B = random.randint(5,95)
                            C = random.randint(5,95)
                            D = random.randint(5,95)
                    elif wylosowane_pytanie[5]=='D':
                        while D<=B or D<=C or D<=A:
                            A = random.randint(5,95)
                            B = random.randint(5,95)
                            C = random.randint(5,95)
                            D = random.randint(5,95)
                print(A, B, C, D)
                kolo_ratunkowe.remove('2. Pytanie do publiczności')
            elif ktore_kolo == '3':
                if wylosowane_pytanie[5] in odp:
                    odp.remove(wylosowane_pytanie[5])
                print('\nProszę o odrzucenie 2 błędnych odpowiedzi.\nDo wyboru pozostały:',wylosowane_pytanie[5],'i',random.choice(odp))
                print()
                kolo_ratunkowe.remove('3. 50:50')
        ilosc_kol -= 1
        print('Pamiętaj - ilość pozostałych kół ratunkowych to:', ilosc_kol)    
    time.sleep(1)
    print(random.choice(jakaodpowiedz))

    odpowiedz = str(input())
    odpowiedz1 = odpowiedz.capitalize() #gdyby gracz wpisał mała a nie duża litere to na wszelki wypadek ją powieksza

    if odpowiedz1 == wylosowane_pytanie[5]: #jeśli odp jest taka sama jak ostatni element listy(czyli poprawna odp)
        print(random.choice(poprawna),'Twoja wygrana to',wygrana,'złotych.')
        if wygrana == '5 000' or wygrana == '75 000':
            print("\nKwota, którą właśnie wygrałeś to kwota gwarantowana.\nOznacza to, że nawet w przypadku przegranej, będziesz mógł zabrać te pieniądze do domu.")
        print()
        time.sleep(1)
        lista_wygrane.remove(wygrana) #usuwamy z listy z sianem pierwszy element, aby nastepnym razem pokazywalo kolejna wygraną
        ilosc_pytan = ilosc_pytan+1 #dodaje jeden aby python wiedzial ze juz na jedno pytanie byla udzieelona odp, kiedy dojdzie do 4 a potem do 8 bd losowalo z kolejnych list
        print(random.choice(prowadzacy),"\n")
    else:
        print("Niestety, odpowiedź której udzieliłeś była niewłaściwa. Poprawna odpowiedź to",wylosowane_pytanie[5])
        if ilosc_pytan>3:
            print("Niemniej jednak, ponieważ dotarłeś do progu kwoty gwarantowanej, twoja wygrana wynosi",gwarantowana[0],", więc nie wychodzisz z pustymi rękami! Gratuluję!")
        elif ilosc_pytan>7:
            print("Niemniej jednak, ponieważ dotarłeś do progu kwoty gwarantowanej, twoja wygrana wynosi",gwarantowana[1],", więc nie wychodzisz z pustymi rękami! Gratuluję!")
        else:
            print("Dziękujemy za udział w grze!")
        break
