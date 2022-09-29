'''
Napiszmy program, który bada podzielność przez 15.
Dla liczb podzielnych przez 3, ale nie przez 5, wypisuje 3.
Dla liczb podzielnych przez 15 wypisuje 15.
Natomiast dla liczb podzielnych przez 5, ale nie przez 3, wypisuje 5.
'''
def main():
    liczba = int(input("Liczba?: "))
    if liczba % 3 == 0 and liczba % 5 != 0:
        print(3)
    elif liczba % 15 == 0:
        print(15)
    elif liczba % 5 == 0 and liczba % 3 != 0:
        print(5)
    else:
        print("nothing")

main()