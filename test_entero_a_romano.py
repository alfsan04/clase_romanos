import pytest
from romano_funcional import entero_a_romano, romano_a_entero, RomanNumberError
"""
Casos de prueba 
a) 1994 -> MCMXCIV
b) 4000 -> RomanNumberError("El valor debe ser menor de 4000")
c) "unacadena" -> RomanNumberError("Debe ser un entero")
d) 0 -> RomanNumberError("El valor debe ser mayor de cero")
e) -3 -> RomanNumberError("El valor debe ser mayor de cero")
f) 4.5 -> RomanNumberError("Debe ser un entero")
"""
def test_1336():
    assert entero_a_romano(1336) == 'MCCCXXXVI'
def test_336(): 
    assert entero_a_romano(336) == 'CCCXXXVI'
def test_romano_a_entero_ordenados():
    assert romano_a_entero('I') == 1
    assert romano_a_entero('MDCCXIII') == 1713
def test_romano_a_entero_no_mas_de_tres():
    with pytest.raises(RomanNumberError) as  exceptionInfo:
        romano_a_entero('LIIII')
    
    assert str(exceptionInfo.value) == "No se pueden dar más de tres repeticiones"
def test_romano_a_entero_resta_si_soy_mayor_que_anterior():
    assert romano_a_entero('IV') == 4   
def test_romano_solo_hasta_un_orden_de_magnitud_en_la_resta():
    with pytest.raises(RomanNumberError) as  exceptionInfo:
        romano_a_entero('IC')
    assert str(exceptionInfo.value) == "I solo se puede restar a V y X"
def test_no_se_puede_repetir_VLD():
    with pytest.raises(RomanNumberError) as  exceptionInfo:
        romano_a_entero('DD')
    assert str(exceptionInfo.value) == "No se puede repetir D"

def test_si_hay_repeticion_no_hay_resta():
    with pytest.raises(RomanNumberError) as  exceptionInfo:
        romano_a_entero('IIX')
    assert str(exceptionInfo.value) == "Si hay repeticion ya no se resta"
