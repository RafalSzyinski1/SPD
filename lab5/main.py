from copy import deepcopy
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


def is_pi_empty(pi):
    for pi_temp in pi:
        if len(pi_temp) != 0:
            return False

    return True


def eval(p, pi, m):
    S = {}
    C = {}

    if is_pi_empty(pi):
        return [S, C, float("inf")]

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
        changes = False
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
                            changes = True
                    else:
                        S[tp] = m_c[p[tp[0]][1][tp[1]]]
                        C[tp] = S[tp] + p[tp[0]][0][tp[1]]
                        m_c[p[tp[0]][1][tp[1]]] = C[tp]
                        changes = True
                last = C[tp]
        if not changes:
            return None  # deadlock
    return [S, C, max(C.values())]


def INSA(p, m):
    tasks = [(i, a[1][0], 0) for i, a in enumerate(p)]
    pi = [[] for _ in range(m)]
    while len(tasks) != 0:
        task = tasks.pop()
        mach = task[1]
        Cmax = float("inf")
        temp_pi = deepcopy(pi)
        for i in range(len(pi[mach]) + 1):
            ttemp_pi = deepcopy(temp_pi)
            ttemp_pi[mach].insert(i, (task[0], task[2]))
            e = eval(p, ttemp_pi, m)
            if (e != None) and (e[2] < Cmax):
                Cmax = e[2]
                pi = deepcopy(ttemp_pi)
        if len(p[task[0]][1]) > task[2] + 1:
            tasks.append((task[0], p[task[0]][1][task[2] + 1], task[2] + 1))
    return [pi, Cmax]


def init(j, m, seed=1):
    rng = RandomNumberGenerator(seed)
    Z = []
    for _ in range(j):
        oj = rng.nextInt(1, int(math.floor(m * 1.2)))
        p = [rng.nextInt(1, 29) for _ in range(oj)]
        u = [rng.nextInt(0, m - 1) for _ in enumerate(range(oj))]
        Z.append([p, u])
    return Z


def main1():
    m = 10
    Z = init(20, m)
    pprint(Z)
    pi, Cmax = INSA(Z, m)
    print(pi, Cmax)
    pprint(eval(Z, pi, m))


if __name__ == '__main__':
    main1()
