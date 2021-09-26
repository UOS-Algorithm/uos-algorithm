n, k = map(int, input().split())
students = [0] * n
length = [0] * 21
result = 0

for rank in range(n):
    l = len(input())
    students[rank] = l
    if rank > k:
        length[students[rank-k-1]] -= 1
    result += length[l]
    length[l] += 1

print(result)