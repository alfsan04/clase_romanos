    # Controla:
    #    - (1) Que no aparezcan carácteres alfabéticos distinto de 'M', 'D', 'C', 'L', 'X', 'V' o 'I'. OK
    #    - (2) Que no se repita más de 3 veces el caracter romano de base 10 (regla 2.1 Ramón). OK
    #    - (3) Que no se repita el caracter romano de base 5 (regla 2.2 Ramón). OK
    #    - (4) Que los caracteres de base 10 solo pueden restar a los caracteres de base 10 y 5 inmediatamente superiores (reglas 3.1, 3.2 y 3.3 Ramón).
    #    - (5) Que los caracteres de base 5 nunca pueden restar (regla 3.4 Ramón).
    #    - (6) No reste más de 1 caracter romano (regla 1 Ramón). 

errores = {
    'error1': 'Caracteres no permitidos',
    'error2': 'Caracter de base 10 repetido mas de 3 veces',
    'error3': 'Caracter de base 5 repetido',
    'error4': 'No se pueden restar esos caracteres',
    'error5': 'Los caracteres de base 5 no pueden restar',
    'error6': 'No puedes restar mas de un caracter romano',
    'error7': 'No puedes duplicar restas iguales'
}

#separar en una lista de sumandos
def separar_sumandos(romano):
    sumandos = []
    par = False
    if len(romano) > 1:
        for pos,i in enumerate(romano):
            indice = lista_romanos.index(i)
            if pos < len(romano) - 1:
                indice_siguiente = lista_romanos.index(romano[pos+1])
            else:
                indice_siguiente = 0
            if indice >= indice_siguiente:
                if par == False:
                    sumandos.append(i)
                else:
                    sumandos.append(romano[pos-1] + i)
                    par = False
            else:
                par = True
        return sumandos
    else:
        sumandos.append(romano)
        return sumandos

#Caracteres no permitidos
def caracteres_no_permitidos(romano):
    for i in romano:
        if i not in lista_romanos:
            return errores['error1']

#Caracter de base 10 repetido 4 veces o de base 5 2 veces
def repetido_mas_de_cuatro(romano):
    contador = 1
    letra_anterior = ''
    for letra in romano:
        if letra == letra_anterior:
            contador += 1
        else:
            contador = 1
        if contador == 4 and lista_romanos.index(letra)%2 == 0:
            return errores['error2']
        elif contador == 2 and lista_romanos.index(letra)%2 == 1:
            return errores['error3']
        letra_anterior = letra

#Resta no permitida
def resta_no_permitida(valores_separados):
    valores_separados_dobles = list(filter(lambda c: len(c) == 2, valores_separados))
    for i in valores_separados_dobles:
        diferencia = lista_romanos.index(i[1]) - lista_romanos.index(i[0])
        if diferencia > 2:
            return errores['error4']

#Caracter de base 5 restando
def caracter_base_cinco_restando(valores_separados):
    valores_separados_dobles = list(filter(lambda c: len(c) == 2, valores_separados))
    for i in valores_separados_dobles:
        if lista_romanos.index(i[0]) % 2 == 1:
            return errores['error5']
    
#funcion para detectar mas de un caracter romano restando
def mas_de_un_caracter_restando(valores_separados):
    for pos, i in enumerate(valores_separados):
        if pos < len(valores_separados) - 1:
            if i == valores_separados[pos+1][0] and len(valores_separados[pos+1]) == 2:
                return errores['error6']

#funcion para detectar restas repetidas
def restas_duplicadas(valores_separados):
    valores_separados_dobles = list(filter(lambda c: len(c) == 2, valores_separados))
    if len(valores_separados_dobles) != len(set(valores_separados_dobles)):
        return errores['error7']

lista_romanos = ('I', 'V', 'X', 'L', 'C', 'D', 'M') #se puede hacer con un string en vez de una tupla: 'IVXLCDM'
romano = 'IIVIV'

valores_separados = separar_sumandos(romano)
print(caracteres_no_permitidos(romano))
print(repetido_mas_de_cuatro(romano))
print(resta_no_permitida(valores_separados))
print(caracter_base_cinco_restando(valores_separados))
print(mas_de_un_caracter_restando(valores_separados))
print(restas_duplicadas(valores_separados))