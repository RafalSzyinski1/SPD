from RandomNumberGenerator import RandomNumberGenerator
from pprint import pprint
from itertools import permutations
from sys import maxsize

def eval(p, pi):
    S = [0]
    C = [p[pi[0]][0]]
    T = [max([C[0] - p[pi[0]][2], 0])]
    F = 0
    
    for order in pi[1:]:
        S.append(C[-1])
        C.append(S[-1] + p[order][0])
        T.append(max([C[-1] - p[order][2], 0]))
        F += T[-1] * p[order][1]
    
    return [S, C, T, F]

def brute_force(p):
    best_pi = [x for x in range(len(p))]
    best_F = maxsize
    for pi in permutations([x for x in range(len(p))]):
        _, _, _, F = eval(p, pi)
        if F < best_F:
            best_F = F
            best_pi = pi[:]
    return best_pi

def greedy(p):
    pi = [x for x in range(len(p))]
    pi.sort(key=lambda x: p[x][2])
    return pi

def sump(D, p):
    counter = 0
    sum = 0
    while D != 0:
        bit = D & 1
        D = D >> 1
        if bit == 1:
            sum += p[counter][0]
        counter += 1
    return sum

def PD(p):
    size = 2**len(p)
    mem = [0 for _ in range(size)]
    for x in range(1, size):
        sumpj = sump(x, p)
        temp = []
        counter = 0
        D = x
        while D != 0:
            bit = D & 1
            D = D >> 1
            if bit == 1:
                temp.append(max([sumpj - p[counter][2], 0]) * p[counter][1] + mem[x - counter])
            counter += 1
        mem[x] = min(temp)
    return mem

def init(j, seed=1, sumx=True):
    rng = RandomNumberGenerator(seed)
    result = [[rng.nextInt(1, 29), rng.nextInt(1, 9), 0] for _ in range(j)]
    A = sum([x[0] for x in result])
    if sumx:
        X = A
    else:
        X = 29
    for p in result:
        p[2] = rng.nextInt(1, X)
    
    return result

def main1():
    p = init(5)
    pprint(p)
    pprint(eval(p, [x for x in range(len(p))]))    
    pi = brute_force(p)
    pprint(pi)
    pprint(eval(p, pi))

def main2():
    p = init(5)
    pprint(p)
    pprint(eval(p, [x for x in range(len(p))]))    
    pi = greedy(p)
    pprint(pi)
    pprint(eval(p, pi))

def main3():
    p = init(5)
    pprint(p)
    print(sump(6, p))

if __name__ == '__main__':
    main3()