from romano_funcional import entero_a_romano, RomanNumberError

class NumeroRomano:
    componentes = {
        1000: 'M', 2000: 'MM', 3000: 'MMM', 
        100: 'C', 200: 'CC', 300: 'CCC',
        400: 'CD', 500: 'D', 600: 'DC',
        700: 'DCC', 800: 'DCCC', 900: 'CM',
        10: 'X', 20: 'XX', 30: 'XXX',
        40: 'XL', 50: 'L', 60: 'LX',
        70: 'LXX', 80: 'LXXX', 90: 'XC',
        1: 'I', 2: 'II', 3: 'III',
        4: 'IV', 5: 'V', 6: 'VI',
        7: 'VII', 8: 'VIII', 9: 'IX'
    } 
    simbolos_romanos  = {
        'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1, '': 0
    }
    restas  = {
        'I': ('V', 'X'), 
        'X': ('L', 'C'), 
        'C': ('D', 'M'), 
    }

    def __init__(self, valor):
        if isinstance(valor, int):
            self.valor = valor
            self.representacion = self.entero_a_romano(valor)
        elif isinstance(valor, str):
            self.representacion = valor
            self.valor = self.romano_a_entero(valor)
        else:
            raise RomanNumberError("Valor debe ser cadena o entero")

    def entero_a_romano(self, valor):
        numero = "{:0>4d}".format(valor)
        digitos = list(numero)
        longitud = len(digitos)
        romano = ''
        for ix in range(len(numero)):
            longitud -= 1
            digitos[ix] = digitos[ix] + "0" * longitud
            romano += self.componentes.get(int(digitos[ix]), "")

        return romano

    def romano_a_entero(self, romano):
        r = 0
        cont_repes = 1
        car_anterior = ""
        car_anteanterior = ""
        for caracter in romano:
            if caracter == car_anterior:
                cont_repes += 1
            else:
                cont_repes = 1 
            if cont_repes > 3:
                raise RomanNumberError("No se pueden dar más de tres repeticiones")
            elif cont_repes == 2 and caracter in "VLD":
                raise RomanNumberError(f"No se puede repetir {caracter}")             
            if car_anterior and self.simbolos_romanos[caracter] > self.simbolos_romanos[car_anterior]:
            # Forma de diccionario restas
                if car_anterior not in self.restas.keys():
                    raise RomanNumberError("El simbolo {} no puede restar".format(car_anterior))
                if caracter not in self.restas[car_anterior]:
                    raise RomanNumberError(f"{car_anterior} solo se puede restar a {self.restas[car_anterior][0]} y {self.restas[car_anterior][1]}")         
                if car_anterior == car_anteanterior:
                    raise RomanNumberError("Si hay repeticion ya no se resta")

                r -= self.simbolos_romanos[car_anterior] * 2

            r += self.simbolos_romanos[caracter]
            car_anteanterior = car_anterior
            car_anterior = caracter

        return r

    def __add__(self, otro):
        if isinstance(otro, NumeroRomano):
            return NumeroRomano(self.valor + otro.valor)
        elif isinstance(otro, int):
            return NumeroRomano(self.valor + otro)

    def __radd__(self, otro):
        #si viene primero el numero y luego el romano en la suma buscara el radd del romano, por lo que podemos llamar desde aqui a add
        return self.__add__(otro)

    def __repr__(self):
        return self.representacion

nr1 = 45 + NumeroRomano(1)
print(nr1)