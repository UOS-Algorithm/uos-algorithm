import sys
sys.setrecursionlimit(200000)

def find_parent(x):
    if parent[x]!=x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int,sys.stdin.readline().split())

parent = [0] * (v+1)

for i in range(1,v+1):
    parent[i] = i


for i in range(e):
    a,b = map(int,sys.stdin.readline().split())
    if find_parent(a) == find_parent(b):
        print(i+1)
        exit()
    else: 
        union_parent(a,b)
    
print(0)