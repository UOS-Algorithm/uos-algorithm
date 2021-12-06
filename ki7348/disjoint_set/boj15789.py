import sys
sys.setrecursionlimit(10**6)

n,m = map(int,sys.stdin.readline().split())

parent = [0] * (n+1)

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

ctp, hansol, ally = map(int,sys.stdin.readline().split())

max_str = 0

for i in range(1,n+1):
    parent[i] = find_parent(i)


set_parent = list(set(parent[1:]))

result = []

for i in set_parent:
    if i != find_parent(hansol) and i != find_parent(ctp):
        result.append(parent.count(i))
        
result.sort()

total = 0

for i in range(ally):
    total+=result.pop()

print(total+parent.count(find_parent(ctp)))