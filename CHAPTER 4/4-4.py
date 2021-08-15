def mysolution():
    n, m = map(int, input().split())
    a, b, d = map(int, input().split())

    gameMap = [[0]*m for _ in range(n)]
    userMap = [[0]*m for _ in range(n)]

    for i in range(n):
        data = list(map(int, input().split()))
        gameMap[i] = data

    # 북 동 남 서 
    direction = [3, 0, 1, 2]
    moveX = [-1, 0, 1, 0]
    moveY = [0, -1, 0, 1]

    count = 0
    direction = 0

    while True:
        d = direction[d]
        idx = direction.index(d)
        nextA = a+moveX[idx]
        nextB = b+moveY[idx]

        if 0<nextA<n and 0<nextB<m and userMap[nextA][nextB]==0:
            a = nextA
            b = nextB
            count += 1
            direction = 1
            userMap[nextA][nextB] = 1
            continue

        if userMap[nextA][nextB] == 1:
            direction += 1
            
        

def solution():
    n, m = map(int, input().split())

    d = [[0]*m for _ in range(n)]
    x, y, direction = map(int, input().split())
    d[x][y] = 1

    array = []
    for i in range(n):
        array.append(list(map(int,input().split())))
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    count = 1
    turn_time = 0
      
    while True:
        direction -= 1
        if direction == -1:
            direction = 3

        nx = x + dx[direction]
        ny = y + dy[direction]

        if d[nx][ny] == 0 and array[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue
        else:
            turn_time+=1

        if turn_time == 4 : 
            nx = x - dx[direction]
            ny = y - dy[direction]

            if array[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn_time = 0

    print(count)

if __name__ == '__main__':
    solution()