import sys
sys.setrecursionlimit(10**6)

n,m = map(int,sys.stdin.readline().split())

planet = []

for _ in range(n):
    planet.append(int(sys.stdin.readline()))
planet = [0] + planet
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
        planet[a] += planet[b]
    else:
        parent[a] = b
        planet[b] += planet[a]


for i in range(1,n+1):
    parent[i] = i


for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    if find_parent(a) != find_parent(b):
        union_parent(a,b)
    print(planet[find_parent(a)])


