import pytest
from checker import checker

@pytest.mark.parametrize("rod_cislo, expected", [
    #?Good ones
    ("2503313483", True),
    ("2505318893", True),
    ("9057145713", "Zenske rodne cislo"),
    ("5757316202", "Zenske rodne cislo"),
    ("0208214347", True),
    ("2501117916", True),
    # #?Bad ones
    ("2513313483", False),
    ("2605318893", False),
    ("8605186111", False),
    ("5763716202", False),
    ("25011179161", False),
    ("6563022921a", False),
])
def test_checker(rod_cislo, expected):
    
    assert checker.check(rod_cislo) == expected
   