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
    c,a,b = map(int,sys.stdin.readline().split())
    if c == 0:
        union_parent(a,b)
    else:
        temp_a = find_parent(a)
        temp_b = find_parent(b)
        if temp_a == temp_b:
            print('YES')
        else:
            print('NO')
            
    