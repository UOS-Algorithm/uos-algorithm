import sys
from math import ceil
n = int(sys.stdin.readline())
arr = []
max_com = 0
sum_arr = 0
for _ in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    if max(temp) > max_com:
        max_com = max(temp)
    sum_arr+=sum(temp)
    arr.append(temp)
start = 0
end = max_com
per_arr = ceil(sum_arr / 2)

while start <= end:
    total = 0
    mid = (start+end) //2

    for i in range(n):
        for j in range(n):
            if arr[i][j] < mid:
                total += arr[i][j]
            else:
                total += mid
    
    if total >= per_arr:
        end = mid - 1
    else:
        start = mid + 1

print(start)
