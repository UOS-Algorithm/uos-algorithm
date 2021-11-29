import sys
sys.setrecursionlimit(300000)

n = int(sys.stdin.readline())

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
    
for i in range(n-2):
    a,b = map(int,sys.stdin.readline().split())
    union_parent(a,b)

temp = find_parent(1)
for i in range(2,n+1):
    if find_parent(i) != temp:
        print(temp,find_parent(i))
        break

            
    