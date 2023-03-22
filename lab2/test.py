import unittest
from main import *


class Test(unittest.TestCase):
    def test1(self):
        n = 10
        rng = RandomNumberGenerator(1)
        Z = [Task(0, rng.nextInt(1, 29), 0, i) for i in range(n)]
        A = sum(x.p for x in Z)
        X = A
        for x in Z:
            x.r = rng.nextInt(1, A)
        for x in Z:
            x.q = rng.nextInt(1, X)
        self.assertEqual(eval(Z), 335)
        self.assertEqual(eval(Schrage(Z)), 213)


if __name__ == "__main__":
    unittest.main()
