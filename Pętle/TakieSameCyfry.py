'''

Sprawdź razem z Bajtkiem ile liczb z podanych 1000 w pliku tekstowym składa się z tych samych cyfr.


'''

def main():
    file = open('te_same_cyfry.txt', 'r')
    suma = 0
    for i in file:
        x= int(i)
        pom = x%10
        ok=True
        while x>9:
            x=x//10
            if pom != x%10:
                ok = False
        if ok == True:
            suma +=1

    print(suma)



main()