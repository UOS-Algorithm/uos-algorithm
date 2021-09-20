import sys
import heapq

case = int(sys.stdin.readline())
hash = {}
sum = 0

def minus(x):
    return -1*x

for _ in range(case):
    gor_list = sys.stdin.readline().split()
    if int(gor_list[0]) == 1:
        name = gor_list[1]
        value = list(map(int, gor_list[3:]))
        target = list(map(minus,value))
        if name in hash:
            for i in target:
                heapq.heappush(hash[name],i)
        else:
            hash[name]=target
    else:
        name = gor_list[1]
        num = int(gor_list[2])
        if name in hash:
            for i in range(min(num,len(hash[name]))):
                a = heapq.heappop(hash[name])
                sum+=abs(a)

                
print(sum)