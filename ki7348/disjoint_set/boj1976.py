import sys
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

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
    
    
for i in range(n): # 0 1 2
    arr = list(map(int,sys.stdin.readline().split()))
    for j in range(len(arr)): # 0 1 2
        if arr[j] == 1:
            union_parent(i+1,j+1)
            
plan = list(map(int,sys.stdin.readline().split()))

state = True

for i in range(len(plan)-1):
    if find_parent(plan[i]) != find_parent(plan[i+1]):
        state = False

if state:
    print('YES')
else:
    print('NO')