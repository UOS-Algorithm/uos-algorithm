s = input()
li = []
answer = ""

for i in s:
    if i in "+-":
        while li and li[-1] != "(":
           answer += li.pop()
        li.append(i)
    elif i in "*/":
        while li and li[-1] in "*/":
            answer += li.pop()
        li.append(i)
    elif i == "(": 
        li.append(i)
    elif i == ")":
        while li and li[-1] != "(":
            answer += li.pop()
        li.pop()
    else:
        answer += i

while li:
    answer += li.pop()

print(answer)