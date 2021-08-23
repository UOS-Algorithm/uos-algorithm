import sys

T = int(input())
for _ in range(T):
    p = sys.stdin.readline().strip();
    n = int(input())
    k = sys.stdin.readline().strip()[1:-1].split(',')

    if p.count('D') > n:
        print('error')
        continue
    
    rev = True
    for i in p:
        if i == 'R':
            rev = not rev
        else:
            x = 0 if rev else -1
            del k[x]
    if rev:
        print('[' + ','.join(k) + ']')
    else:    
        print('[' + ','.join(reversed(k)) + ']')
