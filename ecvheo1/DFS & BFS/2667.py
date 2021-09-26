import sys

def dfs(x, y, k):
    if x <= -1 or y <= -1 or x >= n or y >= n:
        return False
    if graph[x][y] != 1:
        return False
    if graph[x][y] == 1: # elif graph[x][y] == 1:
        graph[x][y] = k
        dfs(x-1, y, k)
        dfs(x, y-1, k)
        dfs(x+1, y, k)
        dfs(x, y+1, k)
        return True


n = int(sys.stdin.readline())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

result = 0
k = 2
for i in range(n):
    for j in range(n):
        if dfs(i, j, k) == True:
            result += 1
            k += 1

print(result)
answer = []
for i in range(2, k):
    sum = 0
    for j in range(n):
        sum += graph[j].count(i)
    answer.append(sum)
answer.sort()
for i in answer:
    print(i)