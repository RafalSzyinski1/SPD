from RandomNumberGenerator import RandomNumberGenerator
from pprint import pprint
import numpy as np
from heapq import heappop, heappush


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


def SchragePmtnAndEval(Z):
    G = []
    N = Z[:]
    N.sort(key=lambda x: x.r)
    t = N[0].r

    Cmax = N[0].r + N[0].p + N[0].q

    pi = []
    while len(G) != 0 or len(N) != 0:
        while len(N) != 0 and N[0].r <= t:
            heappush(G, N[0])
            N.pop(0)
        if len(G) != 0:
            element = heappop(G)
            if len(pi) != 0:
                last = pi[-1]
                if last.q < element.q:
                    t = t + (element.r - last.r) - last.p
                    last.p = last.p - (element.r - last.r)
                    pi.pop()
                    heappush(G, last)
                else:
                    Cmax = max(Cmax, t + element.q)
            t = t + element.p
            pi.append(element)
        else:
            t = N[0].r

    print([x.i for x in pi])
    return Cmax


def Carlier(J):
    pass


if __name__ == "__main__":
    n = 10
    rng = RandomNumberGenerator(7523)
    Z = [Task(0, rng.nextInt(1, 29), 0, i) for i in range(n)]
    A = sum(x.p for x in Z)
    X = A
    for x in Z:
        x.r = rng.nextInt(1, A)
    for x in Z:
        x.q = rng.nextInt(1, X)
    print(Z)
    print(SchragePmtnAndEval(Z))
