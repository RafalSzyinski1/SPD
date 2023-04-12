import numpy as np
import copy
from RandomNumberGenerator import RandomNumberGenerator
from pprint import pprint
import itertools


def eval(p, pi):
    n = len(p[0])

    # init
    p_0 = p[pi[0]]
    sum = 0
    s = []
    for x in p_0:
        s.append(sum)
        sum += x
    S = [s]
    C = [[S[0][i] + p_0[i] for i in range(n)]]

    # eval
    for order in pi[1:]:
        temp_pi = p[order]
        s = []
        c = []
        for i in range(n):
            if i == 0:
                s.append(C[-1][i])
            else:
                s.append(max([c[-1], C[-1][i]]))
            c.append(s[-1] + temp_pi[i])
        S.append(s)
        C.append(c)
    return [S, C]


def Johnson(p):
    n = len(p)
    N = [i for i in range(n)]
    l = 0
    k = n - 1
    pi = [0 for _ in range(n)]
    while len(N) != 0:
        j = -1
        m = 10000
        for i in N:
            if p[i][0] < m:
                m = p[i][0]
                j = i
            if p[i][1] < m:
                m = p[i][1]
                j = i

        if p[j][0] < p[j][1]:
            pi[l] = j
            l += 1
        else:
            pi[k] = j
            k -= 1

        N.remove(j)
    return pi


def brute_force(p):
    Cmax = 10000000000
    pi = [x for x in range(len(p))]
    best_pi = pi[:]
    for per in itertools.permutations(pi):
        _, C = eval(p, per)
        if Cmax > C[-1][-1]:
            Cmax = C[-1][-1]
            best_pi = per[:]
    return best_pi


def Bound0(pi, N, p):
    return eval(p, pi)[-1][-1][-1] + sum([p[i][-1] for i in N])


def Bound1(pi, N, p):
    return max([eval(p, pi)[-1][-1][m] + sum([p[i][m] for i in N]) for m in range(len(p[0]))])


def BnBp(p, j, N, pi, best_pi, LB, UB):

    pi.append(j)
    N.remove(j)

    # print("j", j, "N", N, "pi", pi, "LB", LB, "UB", UB)

    if len(N) != 0:
        LB = Bound1(pi, N, p)
        if LB < UB[0]:
            for i in N:
                BnBp(p, i, N[:], pi[:], best_pi, LB, UB)
    else:
        Cmax = eval(p, pi)[-1][-1][-1]
        if Cmax < UB[0]:
            UB[0] = Cmax
            for i in range(len(pi)):
                best_pi[i] = pi[i]


def BnB(p):
    bestbest_pi = []
    Cmax = 10000000
    N = [i for i in range(len(p))]
    for i in N:
        best_pi = [0 for _ in range(len(p))]
        UB = [400]
        BnBp(p, i, N[:], [], best_pi, 10000000, UB)
        if UB[0] < Cmax:
            bestbest_pi = best_pi[:]
            Cmax = UB[0]
    return bestbest_pi


def init(m, n, seed=1):
    rng = RandomNumberGenerator(seed)
    return [[rng.nextInt(1, 29) for _ in range(m)] for _ in range(n)]


def main():
    # p = [[4, 1], [4, 3], [1, 2], [5, 1]]
    p = init(2, 20, 2)
    pprint(p)
    k = Johnson(p)
    print("pi", k)
    S, C = eval(p, k)
    print("S", S)
    print("C", C)
    print("Cmax", C[-1][-1])


def main2():
    p = init(3, 10, 2)
    pprint(p)
    k = brute_force(p)
    print("pi", k)
    S, C = eval(p, k)
    print("S", S)
    print("C", C)
    print("Cmax", C[-1][-1])


def main3():
    p = init(2, 5, 2)
    pprint(p)
    print(Bound1([0, 1, 2], [3, 4], p))


def main4():
    p = init(3, 10, 2)
    pprint(p)
    k = BnB(p)
    print("pi", k)
    S, C = eval(p, k)
    print("S", S)
    print("C", C)
    print("Cmax", C[-1][-1])


if __name__ == '__main__':
    main3()
