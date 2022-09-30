'''
Napisz program, który dla danej liczby policzy jej magiczność. Magiczność dla liczb
⩽9 wynosi 1. Operacja s(l) - oznacza sumę cyfr liczby l, natomiast m(l)
oznacza magiczność liczby ll.
Dla l ⩾10 wartość m(l)m(l) wynosi m(s(l)) + 1m(s(l))+1

Podaj magiczność liczby 578
'''

def main():
    l = int(input())

    m = 1
    while l > 9:
        m += 1
        x = 0
        while l != 0:
            x += l % 10
            l //= 10
        l = x

    print(m)

main()