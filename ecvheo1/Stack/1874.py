n = int(input())
x = list(int(input()) for _ in range(n))
s = []
answer = []
count = 1
flag = True

for i in x:
    if i >= count:
        for _ in range(i-count+1):
            s.append(count)
            count += 1
            answer.append('+')
    if s[len(s)-1] != i:
        flag = False
        break
    s.pop()
    answer.append('-')

if flag:
    print('\n'.join(answer))
else:
    print('NO')
