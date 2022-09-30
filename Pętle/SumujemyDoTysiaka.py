'''
Bajtek nie ma czasu, zatem tym razem będzie krótko.
Policz sumę liczb naturalnych mniejszych od 1000 i jednocześnie podzielnych przez 13.
'''


def main():
    suma = 0
    i = 0
    while i < 1000:
        # print('i przed ifem', i) //test
        if i % 13 == 0:
            suma += i
        i += 1
    print('suma', suma)


main()
