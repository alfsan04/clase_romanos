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