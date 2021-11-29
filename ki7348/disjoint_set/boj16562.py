import sys
sys.setrecursionlimit(10**6)

n,m,k = map(int,sys.stdin.readline().split())

parent = [0] * (n+1)

cost = list(map(int,sys.stdin.readline().split()))

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(1,n+1):
    parent[i] = i
    
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    union_parent(a,b)

cost = [0] + cost
result = []

for i in range(1,n+1):
    result.append([find_parent(i),cost[i]])


result.sort(key=lambda x:(x[0],x[1]))
check = []
for i in result:
    check.append(i[0])
    
check = list(set(check))

total = 0
for i in result:
    if i[0] in check:
        total+=i[1]
        check.remove(i[0])
        
if total <= k:
    print(total)
else:
    print("Oh no")