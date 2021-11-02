import sys
from itertools import permutations

n = int(sys.stdin.readline())

temp = list(map(int,sys.stdin.readline().split()))

arr = list(permutations(temp,n))

min_val = 0

for i in arr:
    total = 0
    for j in range(1,len(i)):
        total += abs(i[j]-i[j-1])
    min_val = max(min_val,total)

print(min_val)