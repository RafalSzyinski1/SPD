from RandomNumberGenerator import RandomNumberGenerator
from pprint import pprint
import numpy as np
from heapq import heapify, heappop, heappush


class Task:
    def __init__(self, r, p, q, i):
        self.r = r
        self.p = p
        self.q = q
        self.i = i

    def __repr__(self) -> str:
        return f"r: {self.r}, p: {self.p}, q: {self.q}, i: {self.i}"

    def __lt__(self, rhs):
        return self.q > rhs.q


def eval(pi):
    if len(pi) < 2:
        raise Exception("eval: error")
    S = [pi[0].r]
    C = [S[0] + pi[0].p]
    Cmax = C[0] + pi[0].q
    for i in pi[1:]:
        S.append(max(i.r, C[-1]))
        C.append(S[-1] + i.p)
        Cmax = max(Cmax, C[-1] + i.q)
    return Cmax


def Schrage(J):
    G = []
    N = J[:]
    N.sort(key=lambda x: x.r)
    t = N[0].r
    pi = []
    while len(G) != 0 or len(N) != 0:
        while len(N) != 0 and N[0].r <= t:
            heappush(G, N[0])
            N.pop(0)
        if len(G) != 0:
            element = heappop(G)
            pi.append(element)
            t = t + element.p
        else:
            t = N[0]
    return pi


def Carlier(J):
    pass


if __name__ == "__main__":
    n = 10
    rng = RandomNumberGenerator(1)
    Z = [Task(0, rng.nextInt(1, 29), 0, i) for i in range(n)]
    A = sum(x.p for x in Z)
    X = A
    for x in Z:
        x.r = rng.nextInt(1, A)
    for x in Z:
        x.q = rng.nextInt(1, X)
    pprint(Z)
    print(eval(Z))
    a = Schrage(Z)
    pprint(a)
    print(eval(a))


class Test:
    def test1(self):
        n = 10
        rng = RandomNumberGenerator(1)
        Z = [Task(0, rng.nextInt(1, 29), 0) for _ in range(10)]
        A = sum(x.p for x in Z)
        X = 29
        for x in Z:
            x.r = rng.nextInt(1, A)
            x.q = rng.nextInt(1, X)
        pprint(Z)
        print(eval(Z))
