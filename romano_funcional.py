class RomanNumberError(Exception):
    pass

componentes = {
    1000: 'M', 2000: 'MM', 3000: 'MMM', 
    100: 'C', 200: 'CC', 300: 'CCC',
    400: 'CD', 500: 'D', 600: 'DC',
    700: 'DCC', 800: 'DCCC', 900: 'CM',
    10: 'X', 20: 'XX', 30: 'XXX',
    40: 'XL', 50: 'L', 60: 'LX',
    70: 'LXX', 80: 'LXXX', 90: 'XC',
    1: 'I', 2: 'II', 3: 'III',
    4: 'IL', 5: 'V', 6: 'VI',
    7: 'VII', 8: 'VIII', 9: 'IX'
}    

simbolos_romanos = {
    'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1, '': 0
}

def entero_a_romano(numero):
    numero = "{:0>4d}".format(numero)
    digitos = list(numero)

    longitud = len(digitos)
    romano = ''
    for ix in range(len(numero)):
        longitud -= 1
        digitos[ix] = digitos[ix] + "0" * longitud
        romano += componentes.get(int(digitos[ix]), "")

    return romano

def romano_a_entero(romano: str) -> int:
    res = 0
    #variable para guardar el caracter
    anterior = ''
    for i in romano:
        
        #comprobamos si el caracter anterior es el mismo y no es D, L o V
        if i == anterior and i not in ['D','L','V']:
            contador_rep += 1
        #Caso en que la repetición sea de D, L o V
        elif i == anterior:
            return 'La D, la L y la V no se pueden repetir consecutivamente'
        #reseteamos contador
        else:
            contador_rep = 1
        #rompemos el for si el contador pasa de 3
        if contador_rep > 3:
            return 'No se pueden poner más de tres letras seguidas'
            #cambiar por raise RomanNumberError('No se pueden dar más de tres repeticiones')
        
        #Condicional por si hay que restar en vez de sumar
        if simbolos_romanos[i] > simbolos_romanos[anterior]:
            res = res + simbolos_romanos[i]-2*simbolos_romanos[anterior]
        else:
            res += simbolos_romanos[i]

        #recordamos el caracter anterior
        anterior = i

    return res

print(romano_a_entero('XIVV'))
