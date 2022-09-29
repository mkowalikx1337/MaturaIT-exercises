'''
Bitek potrzebuje pomocy w napisaniu bardzo prostego programu. Chodzi o wczytanie liczby całkowitej x i wypisaniu:

"Jestem mała i dzielę się przez 4" , gdy x < 40 i cztery jest dzielnikiem x

"Jestem mała i nie dzielę się przez 4" , gdy x < 40 i cztery nie jest dzielnikiem x

"Jestem duża i dzielę się przez 4" , gdy x >= 40 i cztery jest dzielnikiem x

"Jestem duża i nie dzielę się przez 4" , gdy x >= 40 i cztery nie jest dzielnikiem x

Pomóż Bitkowi pisząc program i wypisując odpowiedź dla liczb 8894 oraz 36. Odpowiedzi oddziel średnikiem.
'''

def main():
    x = int(input("x?: "))
    if x < 40 and x % 4 == 0:
        print('Jestem mała i dzielę się przez 4')
    elif x < 40 and x % 4 != 0:
        print('Jestem mała i nie dzielę się przez 4')
    elif x >= 40 and x % 4 == 0:
        print('Jestem duża i dzielę się przez 4')
    else:
        print('Jestem duża i nie dzielę się przez 4')

main()