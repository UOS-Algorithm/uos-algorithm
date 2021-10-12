import sys
import math
x,y,c = map(float,sys.stdin.readline().split())


start = 0
end = min(x,y)

while start+0.000001 <= end:
    mid = (start+end) / 2

    h1 = math.sqrt(pow(x,2) - pow(mid,2))
    h2 = math.sqrt(pow(y,2) - pow(mid,2))

    d = (h1*h2) / (h1+h2)

    if d<c:
        end = mid
    else:
        start = mid

print("%0.3f" %start)
    