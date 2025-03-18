import unittest
from Lesson15.calc2 import Calc


class TestCalc(unittest.TestCase):
    
    def test_add(self):
        calc = Calc()
        self.assertEqual(calc.add(10,5), 15)    
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-1,-1), -2)

    def test_korene(self):
        calc = Calc()
        self.assertEqual(calc.korene(1, -3, 2), (2.0, 1.0))
        self.assertEqual(calc.korene(1, 2, 1), (-1.0, -1.0))
        self.assertEqual(calc.korene(1, 2, 1), (-1, -1))
        # quad = calc.korene(1, 0, 1)
        # self.assertEqual(quad[0].real, 0)
        # self.assertEqual(quad[0].imag, 1)