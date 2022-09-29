'''
Bajtek napisał kilka sprawdzianów i chciałby wiedzieć jakie ma z nich oceny.
 Wynik ze sprawdzianu to liczba z przedziału [0, 1]. Progi na oceny są stałe i wynoszą:

2: 0.4
3: 0.5
4: 0.75
5: 0.85
6 : 0.95
Wynik sprawdzianu zależy od zdobytych pp punktów (100 możliwych) i pewnego współczynnika kk.
 Wyraża się wzorem w(p, k) = (p/100)^k

Wypisz oceny Bajtka (oddzielone ; ) ze sprawdzianów dla danych (p, k):

20 0.5
31 0.3
49 0.2
89 1.5

'''
import math


def main():
    p = 89
    k = 1.5
    ocena = math.pow((p / 100), k)
    if 0.4 <= ocena < 0.5:
        print(2)
    elif 0.5 <= ocena < 0.75:
        print(3)
    elif 0.75 <= ocena < 0.85:
        print(4)
    elif 0.85 <= ocena < 0.95:
        print(5)
    elif ocena >= 0.95:
        print(6)
    else:
        print(1)


main()
