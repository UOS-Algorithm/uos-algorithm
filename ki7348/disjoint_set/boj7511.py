import sys
sys.setrecursionlimit(10**6)

t = int(sys.stdin.readline())

for z in range(t):
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
        
    for i in range(m):
        a,b = map(int,sys.stdin.readline().split())
        union_parent(a,b)
    
    for i in range(1,n+1):
        parent[i] = find_parent(i)
        
    k = int(sys.stdin.readline())
    
    result = []
    
    for _ in range(k):
        a,b = map(int,sys.stdin.readline().split())
        if find_parent(a) == find_parent(b):
            result.append(1)
        else:
            result.append(0)
            
    print("Scenario {}:".format(z+1))
    for i in result:
        print(i)
    if z != t-1:
        print("")
    