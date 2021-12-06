import sys
sys.setrecursionlimit(10**6)

n,m = map(int,sys.stdin.readline().split())

real = list(map(int,sys.stdin.readline().split()))
real = real[1:]

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
temp = []
for i in range(m):
    party = list(map(int,sys.stdin.readline().split()))
    people = party[1:]
    temp.append(people)
    for j in range(len(people)-1):
        union_parent(people[j],people[j+1])

result = 0

for i in range(len(real)):
    real[i] = find_parent(real[i])

for i in temp:
    state = True
    for j in i:
        if find_parent(j) in real:
            state = False
        else:
            continue
    if state == True:
        result += 1
    else:
        continue  
            
print(result)