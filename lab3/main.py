import numpy as np
import copy
from RandomNumberGenerator import RandomNumberGenerator
from pprint import pprint


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


def init(m, n):
    rng = RandomNumberGenerator(1)
    return [[rng.nextInt(1, 29) for _ in range(m)] for _ in range(n)]


def main():
    # p = [[4, 1], [4, 3], [1, 2], [5, 1]]
    p = init(2, 12)
    pprint(p)
    k = Johnson(p)
    print("pi", k)
    S, C = eval(p, k)
    print("S", S)
    print("C", C)
    print("Cmax", C[-1][-1])


if __name__ == '__main__':
    main()
