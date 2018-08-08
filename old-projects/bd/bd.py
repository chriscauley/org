from collections import defaultdict
import random

DAYS = 365
results = [0 for i in range(DAYS)]
N = 100

for n in range(N):
    bdays = defaultdict(int)
    for i in range(1,DAYS):
        bdays[random.randint(1,DAYS)] += 1
        if len(bdays) != i:
            break
    for _i in range(i,DAYS):
        results[_i] += 1

for n in results[:50]:
    print int(n*100./N)