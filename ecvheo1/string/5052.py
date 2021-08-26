import sys

def consistency(tele):
    for i in range(len(tele)-1):
        if tele[i] == tele[i+1][0:len(tele[i])]:
                print('NO')
                return
    print('YES')
    return

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    tele = list(sys.stdin.readline().rstrip() for _ in range(n))
    tele.sort()
    consistency(tele)