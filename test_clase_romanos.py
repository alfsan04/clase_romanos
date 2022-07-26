from romanos_class import NumeroRomano

def test_crear_instancia_numero_romano():
    nr = NumeroRomano(34)
    otronr = NumeroRomano(30)
    assert str(nr) == 'XXXIV'
    assert str(otronr) == 'XXX'


def test_crear_instancia_numero_romano_desde_cadena():
    nr = NumeroRomano('XXXI')
    assert str(nr) == 'XXXI'
    assert nr.valor == 31


def test_suma_romanos():
    nr1 = NumeroRomano('XX')
    nr2 = 30

    nr3 = nr1 + nr2
    
    assert isinstance(nr3, NumeroRomano) == True
    assert nr3.valor == 50
    assert nr3.representacion == 'L'