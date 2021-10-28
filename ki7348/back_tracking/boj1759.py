import sys
from itertools import combinations

l,c = map(int,sys.stdin.readline().split())

arr = list(sys.stdin.readline().split())
con = []
vowel = []

for i in arr:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowel.append(i)
    else:
        con.append(i)
comb = []
for i in range(1,len(vowel)+1):
    if l - i >= 2:
        comb.append((l-i,i))
final = []
for i in range(len(comb)): # 0 1
    com_comb = list(combinations(con,comb[i][0]))
    vowel_comb = list(combinations(vowel,comb[i][1]))
    temp = []
    for j in com_comb:
        for k in vowel_comb:
            result = list(j+k)
            result.sort()
            temp.append(result)
    for x in temp:
        final.append(x)

final.sort()

for i in final:
    print(''.join(i))
