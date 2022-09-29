'''
Bajtek dostał od Bitka 10 zestawów kart kolekcjonerskich (z najnowocześniejszymi podzespołami komputerowymi).
Każdy zestaw składał się z innej liczby kart. Jako, że Bajtek jest serdecznym przyjacielem,
chce się odwdzięczyć Bitkowi i wręczyć mu 10 zestawów kart kolekcjonerskich (tym razem z akcesoriami dla graczy).

Bajtek za każdy otrzymany od Bitka zestaw z nieparzystą liczbą kart, chce wręczyć mu pięciokrotnie więcej kart,
 a za każdy zestaw z parzystą liczbą kart, Bajtek chciałby wręczyć Bitkowi, dwa razy mniej kart niż otrzymał.

Wczytaj liczbę kart w danych zestawach z pliku tekstowego, i wypisz kolejno,
z ilu kart będą składały się zestawy podarowane przez Bajtka Bitkowi.
Oddziel odpowiedzi średnikami.
'''
from pathlib import Path
def main():

    file = open('nieparzysta_5.txt', 'r')
    t = []
    for i in file:
        t.append(int(i))

    z = []
    for i in t:
        if i % 2 != 0:
            z.append(int(5*i))
        else:
            z.append(int(i/2))

    print(z)

main()