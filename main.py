import sys

from pumpinglema import PumpingLema


if __name__ == '__main__':
    pumping_lema = PumpingLema()

    if len(sys.argv) == 1:
        string = input("Ingrese su cadena: ")
        p = int(input("Ingrese el p: "))
        is_valid = pumping_lema.apply_pumping_lemma(string=string, p=p)
        print(f"¿Cumple con el Lema de Bombeo la cadena '{string}'?", end=' ')
        print("Sí" if is_valid else "No", end='\n\n')

    elif sys.argv[1] == "--test":
        for i in range(10):
            string = ('a' * i)+('b' * i)+('c' * i)
            is_valid = pumping_lema.apply_pumping_lemma(string=string, p=i)
            print(f"¿Cumple con el Lema de Bombeo la cadena '{string}'?",
                  end=' ')
            print("Sí" if is_valid else "No", end='\n\n')
