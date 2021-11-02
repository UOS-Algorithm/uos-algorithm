import sys
from itertools import permutations

n = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))

oper = list(map(int,sys.stdin.readline().split()))
not_zero_oper = []
cnt = 0
for i in oper:
    if i != 0:
        for _ in range(i):
            not_zero_oper.append(cnt)
    cnt+=1

comb_not_zero_oper = list(permutations(not_zero_oper,len(not_zero_oper)))
result = []
for i in comb_not_zero_oper:
    temp = a[0]
    for j in range(0,n-1):
        second = a[j+1]
        if i[j] == 0:
            temp = temp + second
        elif i[j] == 1:
            temp = temp - second
        elif i[j] == 2:
            temp = temp * second
        elif i[j] == 3:
            if temp < 0:
                temp = -(temp)
                temp //= second
                temp = -(temp)
            else:
                temp //= second
    result.append(temp)

result.sort()
print(result[-1])
print(result[0])