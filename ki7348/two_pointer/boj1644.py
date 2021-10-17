import sys

n = int(sys.stdin.readline())

a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i,n+1,i):
            a[j] = False

start = 0
end = 0

total = 0
count = 0

while start < len(primes):
    if total == n:
        count += 1
        total -= primes[start]
        start += 1
    elif total > n or end >= len(primes):
        total -= primes[start]
        start += 1
    elif total < n:
        total += primes[end]
        end+= 1

print(count)