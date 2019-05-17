### milionerzy
import time
import random

### ten mój wstęp trzeba będzie usunąć
zestaw_pytan = ['0.W którym z miast znajdują się korty Flushing Meadows?',
'1.Co jest głównym składnikiem maści ichtiolowej?',
 '2.Który król założył obok Krakowa miasta Kazimierz i Kleparz']

zestaw_odp = [ ['0. w Londynie, w Paryżu,   w Nowym Jorku   , w Wiedniu'],
['1.tlenek cynku, szkielet ryb karpiowatych,   łupki bitumiczne    , tran'],
['2.   Kazimierz III Wielki    , Kazimierz II Sprawiedliwy, Kazimierz I Odnowiciel, Władysław Łokietek ']]

money1 = '1000'
money2 = '5000'
money3 = '10000'
money4 = '40000'
money5 = '75000'
money6 = '100000'
ilosc_kol = 3
kolo_ratunkowe1 = '1: telefon do przyjaciela '
kolo_ratunkowe2 = '2: publicznosc '
kolo_ratunkowe3 = '3: pol na pol '
prawdopodobien = random.random()
p = round(prawdopodobien,2)

prowadzący = ['aha',  'dobrze ci idzie', 'jak sie czujesz, pewnie wspaniale', 'nie mogę pomóc',
'to dużo pieniądzy', 'na pewno znasz odp na to pytanie',  'co zrobisz jak wygrasz', 'czas na przerwe',
'zapraszam na krótka przerwe' ]
 ###jego komentarze
twoje_pieniadze = 'twoja wygrana to na razie'
poprawna = 'to poprawna odp,'
zla = 'niestety zla odp'
koniec = ' koniec gry, dziekuje za udzial'
nastepne = 'oto kolejne pytanie'
czy_chce_kolo_ratunkowe = 'jesli chcesz skorzystac z kola wcisnij "q" '


print('czytam zasady gry:\nw grze sa zawsze 4 odp a, b, c, d,\nmasz też do dyspozycji 3 kola ratunlkowe:\n',kolo_ratunkowe1,', ',kolo_ratunkowe2,', ', kolo_ratunkowe3)
print('gotowy/gotowa?\nzaczynajmy, gramy o milion zlotych!')
print('czytam pierwsze pytanie')
print()

wylosowane_pytanie = random.choice(zestaw_pytan)
print(wylosowane_pytanie)
print()
print(random.choice(prowadzący))
numer_pytania = zestaw_pytan.index(wylosowane_pytanie)
print(numer_pytania)
print()
print(zestaw_odp[numer_pytania])
print(random.choice(prowadzący))


print(czy_chce_kolo_ratunkowe)
odp_na_kolo_ratunkowe = input()
if odp_na_kolo_ratunkowe == 'q':
	print('OK, ktore kolo wybierasz? ', kolo_ratunkowe1, kolo_ratunkowe2, 'czy ', kolo_ratunkowe3, '?')
	ktore_kolo = str(input())
	if ktore_kolo == '1':
		print('wiec dzwonimy do twojego przyjaciela')
	elif ktore_kolo == '2':
		print('poprosimy o pomoc publicznosc')
	elif ktore_kolo == '3':
		print('wiec odrzucam dwie bledne odpowiedzi')
		print()
print('jaka jest ostateczna odpowiedz?')
ostateczna = input()


if ostateczna == 'a' or ostateczna == 'A':
	print(poprawna, twoje_pieniadze, money1, nastepne,)

elif ostateczna == 'b' or ostateczna == 'c' or ostateczna == 'd' or ostateczna == 'B' or ostateczna == 'C' or ostateczna == 'D':
	print(zla, koniec)
else:
	print('sa tylko 4 mozliwoasi: a, b, c lub d')
