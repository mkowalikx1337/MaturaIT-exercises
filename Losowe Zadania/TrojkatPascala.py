def test(t):
    print('   '.join([str(item) for item in t]).center(150))


def main():
    x = input("Wpisz liczbe poziomów")
    t = [1]
    test(t)
    for i in range(int(x) - 1):
        t1 = [1]
        for j in range(len(t) - 1):
            t1.append(t[j] + t[j + 1])
        t1.append(1)
        t = t1
        test(t)

main()
