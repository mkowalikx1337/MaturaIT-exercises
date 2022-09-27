'''Bitek ma za zadanie policzyć resztę z dzielenia przez 327 z liczby
 ((((49343−23343+46632)⋅8)−330)⋅16−99)÷100

Dasz radę mu w tym pomóc?'''

def main():
    x = ((((49343-23343+46632)*8)-330)*16-99)/100
    print(x%327)

main()