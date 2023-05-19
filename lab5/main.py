from RandomNumberGenerator import RandomNumberGenerator

import math
from pprint import pprint

m1 = (1, 1, 2)
m2 = (1, 2, 3)
m3 = (3)


def eval(p, pi, m):
    processed = [[(-1, -1), 0]]
    graph = {(-1, -1): set()}
    # init start point of graph
    for m_pi in pi:
        for i in range(m):
            if p[m_pi[0][0]][1][0] == i:
                graph[(-1, -1)].add((m_pi[0][0], 0))
    # init machin order for tasks
    for (i, w) in enumerate(p):
        for (j, v) in enumerate(zip(w[0], w[1])):
            processed.append([(i, j), float("inf")])
            if j + 1 < len(w[1]):
                if graph.get((i, j)) == None:
                    graph.update({(i, j): set()})
                graph[(i, j)].add((i, j+1))
    # init pi order for tasks
    for (i, m_pi) in enumerate(pi):
        for tp in zip(m_pi[:-1], m_pi[1:]):
            if tp[0][0] == tp[1][0]:
                if tp[0][1] != tp[0][1] - 1:
                    continue
            if graph.get(tp[0]) == None:
                graph.update({tp[0]: set()})
            graph[tp[0]].add(tp[1])

    pprint(graph)
    pprint(processed)

    m_c = [0 for _ in range(m)]
    # eval


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
    pi = (((0, 0), (0, 2), (1, 0)), ((0, 1), (2, 1), (1, 1)), ((2, 0), (1, 2)))
    pprint(Z)
    pprint(pi)
    pprint(eval(Z, pi, 3))


if __name__ == '__main__':
    main1()
