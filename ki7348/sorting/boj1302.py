import sys
import operator

case = int(sys.stdin.readline())

dict = {}
for _ in range(case):
    name = sys.stdin.readline().strip()
    if name not in dict:
        dict[name] = 1
    else:
        dict[name] += 1

arr = []
for i in dict:
    arr.append((i,dict[i]))

arr.sort(key= lambda x : (-x[1],x[0]))

print(arr[0][0])