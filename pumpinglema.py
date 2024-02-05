import re


class PumpingLema:
    def apply_pumping_lemma(self, string: str, p: int):
        print(f"1. Suponemos que '{string}' esta en el lenguaje "
              "L = {a^n b^n c^n / n >= 0}")

        if not bool(re.match(r'^(a+)(b+)(c+)$', string)):
            print("2. La cadena no contiene solo 'a's, 'b's y 'c's.")
            return
        print("2. La cadena contiene solo 'a's, 'b's y 'c's.")

        if not (string.count("a") == string.count("b") == string.count("c")):
            print("3. La cantidad de 'a's, 'b's y 'c's no son iguales.")
            return
        print("3. La cantidad de 'a's, 'b's y 'c's son iguales.")

        a_part = string[:string.index('b')]
        bc_part = string[string.index('b'):]
        b_part = bc_part[:bc_part.index('c')]
        c_part = bc_part[bc_part.index('c'):]

        u, v, w, x, y = a_part[:p], a_part[p:], b_part, c_part[:p], c_part[p:]

        print("Paso 4: Descomponemos la cadena en las partes u, v, w, x, y:")
        print(f"u = '{u}'")
        print(f"v = '{v}'")
        print(f"w = '{w}'")
        print(f"x = '{x}'")
        print(f"y = '{y}'")

        for i in range(2, 5):
            pumped_string = u + (v * i) + w + (x * i) + y
            if not self._is_in_languaje(string=pumped_string):
                print(f"Paso 5: La cadena '{pumped_string}' obtenida "
                      "al bombear 'v' y 'x' no está en L.")
                return

        print("Paso 5: Todas las cadenas obtenidas al bombear 'v' y 'x' "
              "están en L.")
        return True

    def _is_in_languaje(self, string: str):
        return bool(re.match(r'^(a+)(b+)(c+)$', string)) and \
            string.count("a") == string.count("b") == string.count("c")
