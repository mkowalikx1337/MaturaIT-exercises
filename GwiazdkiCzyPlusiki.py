'''Bajtek lubi i gwiazdki, i plusiki. Jest ciekawy, które z nich wygenerują mu większą liczbę.

Na wejściu (dane w pliku tekstowym) Bajtek dostaje 5 par liczb całkowitych. Jego zadaniem jest wypisanie
dla każdej z par - maksimum z pierwszego elementu w parze zwiększonego o 10 oraz z drugiego elementu podniesionego do
potęgi drugiej.

Pomóż Bajtkowi z tym zadaniem, i wypisz maksima dla każdej linii oddzielone średnikiem.

'''

def main():
    print(max(1 + 10, 3 ** 2))
    print(max(787 + 10, 28 ** 2))
    print(max(394 + 10, 21 ** 2))
    print(max(-1 + 10, (-4) ** 2))
    print(max(123 + 10, 35 ** 2))


main()