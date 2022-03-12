from random import randint,seed
import sys

def try_max(equals, notequals, N, L, K, R):
    equals_f = sorted([(k, v) for k, v in equals.items()], key=lambda x: len(x[1]), reverse=True)
    for eq_entry in equals_f:
        As = eq_entry[0]
        if (len(equals[As]) > 0 and len(notequals[As]) < N*(K-1)//(K) + R):
            return As
    return None

def try_question(equals, notequals, N, L, K, R):

    loops = N*5
    while loops > 0:
        loops -= 1
        As = try_max(equals, notequals, N, L, K, R)
        if (As == None):
            As = randint(1,N*(K-1)//(K))-1
        Bs = randint(1,N)-1

        if (Bs == As):
            continue
        if len(notequals[As]) >= N*(K-1)//K + R:
            continue
        if len(notequals[Bs]) >= N*(K-1) //K + R:
            continue

        if As in equals[Bs] or Bs in equals[As]:
            continue
        if As in notequals[Bs] or Bs in notequals[As]:
            continue
        return (As, Bs)
    return None

def tryGuess(equals_s, notequals, N,L, K):
    #print(equals_s, file=sys.stderr)
    equals_f = [(k,v) for k,v in equals_s.items() if (len(v) >= N//K + L  )]
    if len(equals_f) > 0:
        return equals_f[0][0]
    else:
        return None

def doGuess(equals_s, notequals, N, L, K, R):

    equals_f = sorted([(k,v) for k,v in equals_s.items()], key=lambda x : len(x[1]), reverse=True)
    for eq_entry in equals_f:
        As = eq_entry[0]
        if (len(equals[As]) > 0 and len(notequals[As]) < N*(K-1)//(K)+R ):
            return As
    return None




N, pl_flag, L, K, L_max = map(int, input().split())
D = int(input())
allconds = []

min_guesses = (L + 1) * N / 2

equals, notequals = {k:set() for k in range(N)},{k:set() for k in range(N)}
for i in range(D):
    As, Bs, resp = input().split()
    A, B = int(As), int(Bs)
    allconds.append({"A": A, "B": B, "R": 1 if resp == 'YES' else 0})

for cond in allconds:
    if cond["R"] == 1:
        equals[cond["A"]].add(cond["B"])
        equals[cond["B"]].add(cond["A"])
    else:
        notequals[cond["A"]].add(cond["B"])
        notequals[cond["B"]].add(cond["A"])

while True:
    added = False
    for k,v in equals.items():
        for ve in v:
            if ve not in equals[k]:
                equals[k].add(ve)
                added = True
            if k not in equals[ve]:
                equals[ve].add(k)
                added = True
#            notequals[ve] = notequals[ve].union(notequals[k])
#            notequals[k] = notequals[k].union(notequals[ve])

    if not added:
        break



from itertools import combinations
if (K == 2):
    while True:
        added = False
        for k, v in notequals.items():

            eqc = combinations(v,2)
            for eq in eqc:
                if eq[0] not in equals[eq[1]]:
                    equals[eq[1]].add(eq[0])
                    added = True
                if eq[1] not in equals[eq[0]]:
                    equals[eq[0]].add(eq[1])
                    added = True
        if not added:
            break

#print("EQUALS ",equals, file=sys.stderr)
#print("NOTEQUALS ",notequals, file=sys.stderr)
max_guesses = min_guesses*5
tg = tryGuess(equals, notequals, N, L, K)
if (tg != None):
    print(tg)
else:
    done = False
    R = 0
    while not done:
        if (D < max_guesses):
            tq = try_question(equals, notequals, N, L, K, R)
        else:
            tq = None
        if (tq != None):
            print(tq[0], tq[1])
            done = True
        else:
            tg = doGuess (equals, notequals, N, L, K, R)
            if (tg != None):
                print(tg)
                done = True
        R += 1
