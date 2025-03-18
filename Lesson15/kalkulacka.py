#import JUnit
import cmath

class calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def pythagorean(self, a, b):
        return cmath.sqrt(a**2 + b**2)

    def quadratic(self, a, b, c):
        d = (b**2) - (4*a*c)
        root1 = int((-b - cmath.sqrt(d)) / (2*a))
        root2 = int((-b + cmath.sqrt(d)) / (2*a))
        return (root1,root2)

# kallkualtor = calculator()
# print(kallkualtor.quadratic(4,4,1))
# print(kallkualtor.pythagorean(12,5))
# print(kallkualtor.add(3,4))
# print(kallkualtor.multiply(3,4))