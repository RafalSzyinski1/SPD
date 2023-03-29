from RandomNumberGenerator import RandomNumberGenerator
from pprint import pprint
import numpy as np
from heapq import heappop, heappush
import copy


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


def evalC(pi):
    if len(pi) < 2:
        raise Exception("eval: error")
    S = [pi[0].r]
    C = [S[0] + pi[0].p]
    Cmax = C[0] + pi[0].q
    for i in pi[1:]:
        S.append(max(i.r, C[-1]))
        C.append(S[-1] + i.p)
        Cmax = max(Cmax, C[-1] + i.q)
    return C


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
            t = N[0].r
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

    return Cmax


def Carlier(J, bpi=[], LB=0, UB=100000000000):
    pi = Schrage(J)
    U = eval(pi)
    if U < UB:
        UB = U
        bpi = copy.deepcopy(pi)

    C = evalC(pi)
    piC = zip(pi, C)
    b = np.argmax([x[1] + x[0].q for x in piC])
    a = np.argmin([pi[j].r + sum([x.p for x in pi[j:b]])
                  for j in range(0, b)])
    c = -1
    max_q = -1
    for j in range(a, b):
        if pi[j].q < pi[b].q and pi[j].q > max_q:
            c = j
            max_q = pi[j].q
    if c == -1:
        return bpi
    K = range(c, b + 1)
    br = min([pi[j].r for j in K])
    bq = min([pi[j].q for j in K])
    bp = sum([pi[j].p for j in K])

    temp_r = pi[c].r
    pi[c].r = max([pi[c].r, br + bp])

    LB = SchragePmtnAndEval(pi[:])

    if LB < UB:
        Carlier(pi, bpi, LB, UB)

    pi[c].r = temp_r

    temp_q = pi[c].q
    pi[c].q = max([pi[c].q, bq + bp])

    LB = SchragePmtnAndEval(pi[:])

    if LB < UB:
        Carlier(pi, bpi, LB, UB)

    pi[c].q = temp_q
    return bpi


if __name__ == "__main__":
    n = 12
    rng = RandomNumberGenerator(1)
    Z = [Task(0, rng.nextInt(1, 29), 0, i) for i in range(n)]
    A = sum(x.p for x in Z)
    X = A
    for x in Z:
        x.r = rng.nextInt(1, A)
    for x in Z:
        x.q = rng.nextInt(1, X)
    pprint(Z)
    a = [5, 1, 2, 7, 6, 8, 3, 10, 4, 9, 0, 11]
    pprint(evalC([Z[i] for i in a]))
    print(eval([Z[i] for i in a]))
    b = Carlier(Z)
    pprint(b)

    print(eval(Z))
