'''
Pomóż Bitkowi i Bajtkowi policzyć stopień podobieństwa ich hasełek.

Hasełko Bitka: "wfnjsdneinvrefmemcicmiircedjnddjjmxsxwp" Hasełko Bajtka: "anhnfdiacidmcdmcodcpmwsicmwdimcwmic"

Stopień podobieństwa jest liczony w następujący sposób. Dla każdej litery( jeśli mamy np. 3 litery "w" w danym słowie,
 rozpatrujemy je osobno) w haśle Bitka, dodajemy do wyniku liczbę jej powtórzeń w haśle Bajtka.

Dla przykładu, dla hasełek: "abcdb" i "bcgf"

Stopień podobieństwa wynosi: 3
'''

def main():
    bitek = 'wfnjsdneinvrefmemcicmiircedjnddjjmxsxwp'
    bajtek = 'anhnfdiacidmcdmcodcpmwsicmwdimcwmic'

    bx = len(bitek)
    print(bx)
    by = len(bajtek)

    z = 8
    suma = 0
    for i in bitek:
        for j in bajtek:
            if i == j:
                suma += 1

    print(suma)
main()