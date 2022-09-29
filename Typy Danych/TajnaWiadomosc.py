import base64
'''Bajtek odnalazł zaszyfrowaną wiadomość i klucz użyty do jej utworzenia. Wie jaka metoda została użyta do szyfrowania,
    ale nie potrafi dokończyć obliczeń, dlatego zwrócił się do Ciebie. Proces odczytu wiadomości wygląda następująco:

klucz i zaszyfrowana wiadomość to liczby zapisane szesnastkowo
odczyt wiadomości polega na wykonaniu operacji xor (^) na kluczu i zaszyfrowanej wiadomości
uzyskany wynik należy skonwertować do postaci szesnastkowej -> h
następnie skonwertować h na tekst za pomocą funkcji base64.b16decode(h)
Odszyfruj wiadomość dla danych:

klucz = 584b51f48bca9572acd08d378362
zaszyfrowana = 2e2e3f9dabbcfc16c5f0fb5ee00b
Uwagi:

Aby użyć funkcji b16decode, na początku programu napisz: import base64
Funkcja b16decode akceptuje tylko wielkie litery, możesz wykorzystać funkcję upper(), np. "abc".upper() -> "ABC" '''

def main():
    key = int(input("key: "), 16)
    enc = int(input("enc msg: "), 16)
    dec = key ^ enc
    h = hex(dec)[2:].upper() # pozbywam się 0x z początku i zmieniam znaki na wielkie
    print(base64.b16decode(h).decode())

main()