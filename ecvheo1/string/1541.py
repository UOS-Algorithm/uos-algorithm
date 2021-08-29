a = list(input().split('-'))
k = list(a[0].split('+'))
sum = 0
for i in k:
    sum += int(i)
for i in range(1, len(a)):
    x = list(a[i].split('+'))
    for j in x:
        sum -= int(j) 
print(sum)