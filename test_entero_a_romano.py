import pytest

from romano_funcional import entero_a_romano, romano_a_entero

def test_1336():
    assert entero_a_romano(1336) == 'MCCCXXXVI'

def test_336():
    assert entero_a_romano(336) == 'CCCXXXVI'

def test_romano_a_entero_ordenados():
    assert romano_a_entero('I') == 1
    assert romano_a_entero('MDCCXIII') == 1713

'''
def test_romano_a_entero_no_mas_de_tres():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero('LIIII')

    assert str(exceptionInfo) == 'No se pueden dar más de tres repeticiones'
'''

def test_romano_a_entero_resta_si_soy_mayor_que_anterior():
    assert romano_a_entero('IV') == 4