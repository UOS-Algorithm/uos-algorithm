import sys

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [0, -1, 1, -1, 1, -1, 0, 1]

def dfs(x,y):
    if x<0 or x>=m or y<0 or y>=n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(8):
            dfs(x+dx[i],y+dy[i])
        return True


while True:
    n, m = map(int,sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    
    graph = []
    total = 0
    for i in range(m):
        graph.append(list(map(int,sys.stdin.readline().split())))

    
    for i in range(m):
        for j in range(n):
            if dfs(i,j)==True:
                total+=1

    print(total)