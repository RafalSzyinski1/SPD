from RandomNumberGenerator import RandomNumberGenerator

import math
from pprint import pprint
import numpy as np

m1 = (1, 1, 2)
m2 = (1, 2, 3)
m3 = (3)


def is_valid_pi(pi):
    for m_pi in pi:
        tasks = {}
        for tp in m_pi:
            if tp[0] not in tasks:
                tasks[tp[0]] = tp[1]
            else:
                if tp[1] <= tasks[tp[0]]:
                    return False
                else:
                    tasks[tp[0]] = tp[1]
    return True


def eval(p, pi, m):
    S = {}
    C = {}

    if not is_valid_pi(pi):
        return None

    m_c = [0 for _ in range(m)]
    for m_pi in pi:
        for j, tp in enumerate(m_pi):
            if j == 0 and tp[1] == 0:
                C.update({tp: p[tp[0]][0][tp[1]]})
                S.update({tp: 0})
                m_c[p[tp[0]][1][tp[1]]] = p[tp[0]][0][tp[1]]
            else:
                C.update({tp: -1})
                S.update({tp: -1})
    while -1 in C.values():
        for m_pi in pi:
            last = 0
            for tp in m_pi:
                if C[tp] == -1 and last != -1:
                    if tp[1] - 1 >= 0:
                        if (tp[0], tp[1] - 1) not in C:
                            return None
                        if C[(tp[0], tp[1] - 1)] != -1:
                            S[tp] = max(
                                [m_c[p[tp[0]][1][tp[1]]], C[(tp[0], tp[1] - 1)]])
                            C[tp] = S[tp] + p[tp[0]][0][tp[1]]
                            m_c[p[tp[0]][1][tp[1]]] = C[tp]
                    else:
                        S[tp] = m_c[p[tp[0]][1][tp[1]]]
                        C[tp] = S[tp] + p[tp[0]][0][tp[1]]
                        m_c[p[tp[0]][1][tp[1]]] = C[tp]
                last = C[tp]
    return [S, C, max(C.values())]


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
    Z = [[[2, 2, 2], [0, 1, 0]], [[3, 3, 3], [0, 1, 2]], [[4, 4], [2, 1]]]
    pi = (((0, 0), (0, 2)), ((0, 1),), ((1, 1), ))
    pprint(Z)
    pprint(pi)
    pprint(eval(Z, pi, 3))


if __name__ == '__main__':
    main1()
