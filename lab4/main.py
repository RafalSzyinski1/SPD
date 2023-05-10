from RandomNumberGenerator import RandomNumberGenerator
from pprint import pprint
from itertools import permutations
from sys import maxsize
import numpy as np
import time

def eval(p, pi):
    S = [0]
    C = [p[pi[0]][0]]
    T = [max([C[0] - p[pi[0]][2], 0])]
    F = T[-1] * p[pi[0]][1]
    
    for order in pi[1:]:
        S.append(C[-1])
        C.append(S[-1] + p[order][0])
        T.append(max(C[-1] - p[order][2], 0))
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
    mem_last = [0 for _ in range(size)]
    for x in range(1, size):
        sumpj = sump(x, p)
        temp = []
        temp_last = []
        counter = 0
        D = x
    #    print(f"x: {x} = {bin(x)}, sumpj: {sumpj}")
        while D != 0:
            bit = D & 1
            D = D >> 1
            if bit == 1:
    #            print(f"\tF({bin(x & ~(1 << counter))}) = {mem[x & ~(1 << counter)]}, j: {counter}")
                temp.append(max(sumpj - p[counter][2], 0) * p[counter][1] + mem[x & ~(1 << counter)])
                temp_last.append(counter)
            counter += 1
        arg = np.argmin(temp)
        mem[x] = temp[arg]
        mem_last[x] = temp_last[arg]
    #    print(f"RESULT: F({bin(x)}) = {mem[x]}")
    #print(mem)
    #print(mem_last)
    pi = []
    index = size - 1
    for _ in range(len(p)):
        value = mem_last[index]
        pi.insert(0, value)
        index = index & ~(1 << value)
     #   print(f"F({bin(index)}) = {index}")
    return mem[-1], pi

def init(j, seed=1, sumx=True):
    rng = RandomNumberGenerator(seed)
    result = [[rng.nextInt(1, 29), 0, 0] for _ in range(j)]
    for p in result:
        p[1] = rng.nextInt(1, 9)
    A = sum([x[0] for x in result])
    if sumx:
        X = A
    else:
        X = 29
    for p in result:
        p[2] = rng.nextInt(1, X)
    
    return result

def main1():
    p = init(5, seed=2)
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
    p = init(5, seed=2)
    pprint(p)
    f, pi = PD(p)
    print("F = ", f)
    pprint(pi)
    pprint(eval(p, pi)[-1])
    
if __name__ == '__main__':
    main1()
    print('//////////////////')
    main3()