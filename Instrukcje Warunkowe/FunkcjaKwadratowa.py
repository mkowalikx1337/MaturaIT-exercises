'''
Napisz program, który wczyta współczynniki funkcji kwadratowej ax^2 + bx + c
i wyznaczy jej miejsca zerowe z dokładnością do 2 miejsc po przecinku lub stwierdzi,
 że nie ma ona (rzeczywistych miejsc) zerowych.

Przykładowe dane:

1
1
-6

Wynik działania:

-3.00; 2.00;

W odpowiedzi podaj w kolejności rosnącej wynik działania programu dla danych:

1053
414
33
'''
from math import sqrt


def delta(a, b, c):
    return sqrt(pow(b, 2) - 4*a*c)


def miejscaZerowe(a, b, c):
    if delta(a, b, c) < 0:
        print("Brak miejsc zerowych")
    elif delta(a, b, c) == 0:
        wynik = -b / (2 * a)
        print(wynik)
    else:
        wynik1 = (-b - delta(a, b, c)) / (2 * a)
        wynik2 = (-b + delta(a, b, c)) / (2 * a)
        print(round(wynik1, 2), round(wynik2, 2))


def main():
    a = 1053
    b = 414
    c = 33
    # print(delta(a, b, c))
    miejscaZerowe(a, b, c)


main()
