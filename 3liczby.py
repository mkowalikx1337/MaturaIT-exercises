'''Bitek od zawsze chciał tworzyć niesamowite narzędzia. Początki, jednak, nie zawsze są łatwe.
Czy pomożesz mu w zaimplemetnowaniu "Konwertinatora"?

W pliku tekstowym dostaniesz 3 liczby w systemie dziesiętnym:

a) pierwszą z nich wypisz w systemie szesnastkowym,

b) drugą z nich wypisz w systemie ósemkowym,

c) trzecią z nich wypisz w systemie dwójkowym.

Za pomocą "Konwertinatora" podaj ich odpowiedniki w odpowiednich systemach oddzielone średnikami.'''


def main():
    number1 =  1011
    number2 = 9999
    number3 = 1923132321

    print(hex(number1), oct(number2), bin(number3))

main()
