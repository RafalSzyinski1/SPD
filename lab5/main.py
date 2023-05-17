from RandomNumberGenerator import RandomNumberGenerator

import math
from pprint import pprint

m1 = (1, 1, 2)
m2 = (1, 2, 3)
m3 = (3)

def eval(p, pi):
    pass

def init(j, m, seed=1):
    rng = RandomNumberGenerator(seed)
    Z = []
    for _ in range(j):
        oj = rng.nextInt(1, int(math.floor(m * 1.2)))
        p = [rng.nextInt(1, 29) for _ in range(oj)]
        u = [rng.nextInt(0, m - 1) for _ in range(oj)]
        Z.append([p, u])
    return Z

def main1():
    Z = init(10, 3)
    pprint(Z)
    pprint(eval())

if __name__ == '__main__':
    main1()