n = int(input())
p = list(map(int, input().split()))

sumMinute = 0
result = []
p.sort()
for i in p:
    sumMinute = sumMinute + i
    result.append(sumMinute)

print(sum(result))
