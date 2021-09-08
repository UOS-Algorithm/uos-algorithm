n = int(input())
board = [[0] * n for _ in range(n)]
direction = []

k = int(input())
for _ in range(k):
    row, column = map(int, input().split())
    board[row-1][column-1] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    direction.append([int(x), c])

snake = [[0, 0]]
time = 0
a, b = 0, 1

while True:
    time += 1
    if a == 0 and b == 1:
        headOne = snake[len(snake)-1][0]
        headTwo = snake[len(snake)-1][1] + 1
    elif a == 0 and b == -1:
        headOne = snake[len(snake)-1][0]
        headTwo = snake[len(snake)-1][1] - 1
    elif a == 1 and b == 0:
        headOne = snake[len(snake)-1][0] + 1
        headTwo = snake[len(snake)-1][1]
    else: # a == -1 and b == 0
        headOne = snake[len(snake)-1][0] - 1
        headTwo = snake[len(snake)-1][1]
    snake.append([headOne, headTwo])
    if (headOne < 0 or headOne >= n or headTwo < 0 or headTwo >= n) or (snake[len(snake)-1] in snake[:len(snake)-2]):
        break
    if board[headOne][headTwo] != 1:
        del snake[0]
    else:
        board[headOne][headTwo] = 0

    if direction and (time == direction[0][0]):
        if direction[0][1] == 'D':
            if a == 0:
                a, b = b, a
            else:
                a, b = b, -a
        else:
            if a == 0:
                a, b = -b, a
            else:
                a, b = b, a
        del direction[0]

print(time)