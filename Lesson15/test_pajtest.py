import pytest
from calc2 import Calc
from zadanie1 import integers

@pytest.mark.parametrize("mnozina,expected",[
    ([2,2,2],6),
    ([-1,1,0],0),    
    ])
def test_sum(mnozina, expected):
    mnoz = integers(mnozina)
    assert mnoz.sum() == expected
@pytest.mark.parametrize("mnozina,expected",[
    ([50,20,30],50),
    ([1,15,35],35)])
def test_max(mnozina,expected):
    mnoz = integers(mnozina)
    assert mnoz.max() == expected
@pytest.mark.parametrize("mnozina,expected",[
    ([100,-200,20,0],-200),
    ([1,2,3,4,5],1)])
def test_min(mnozina,expected):
    mnoz = integers(mnozina)
    assert mnoz.min() == expected
@pytest.mark.parametrize("mnozina,expected",[
    ([1,2,3,4,5],3),
    ([1,2,3,4,5,6],3.5)])
def test_avrg(mnozina,expected):
    mnoz = integers(mnozina)
    assert mnoz.avrg() == expected

# def test_add(a,b,expected):
#     calc = Calc()
#     assert calc.add(a,b) == expected
    # assert calc.add(10,5) == 15
    # assert calc.add(-1,1) == 0
    # assert calc.add(-1,-1) == -2

