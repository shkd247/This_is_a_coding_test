
def mysolution():
    n = int(input())
    path = list(input().split())

    x=1
    y=1
    nextX=0
    nextY=0

    for i in path:
        if i == 'L':
            nextY = y-1
        elif i == 'R':
            nextY = y+1
        elif i == 'U':
            nextX = x-1
        elif i == 'D':
            nextX = x+1

        if 0<nextX<=n:
            x = nextX
        if 0<nextY<=n:
            y = nextY

    print(x, y)

def solution():
    n = int(input())
    x, y = 1, 1
    plans = input().split()

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L','R','U','D']

    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx<1 or ny<1 or nx>n or ny>n:
            continue

        x, y = nx, ny
    
    print(x, y)


if __name__ == "__main__":
    mysolution()