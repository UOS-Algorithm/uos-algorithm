n = int(input())
tower = list(map(int, input().split()))
k = [0]
answer = [0]
for i in range(1, n):
    if tower[k[-1]] > tower[i]:
        answer.append(k[-1] + 1)
        k.append(i)
    else:
        k.pop()
        while len(k) > 0 and tower[k[-1]] < tower[i]:
            k.pop()
        if len(k) == 0:
            answer.append(0)
        else:
            answer.append(k[-1] + 1)
        k.append(i)
        
print(' '.join(map(str, answer)))