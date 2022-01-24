from collections import deque
 
# 보드 크기
n = int(input())
board = [[0]*n for _ in range(n)]

# 사과 개수
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1 

# 방향 정보 
l = int(input())
direction = dict()
for _ in range(l):
    x, y = input().split()
    direction[int(x)] = y

dict = dict()
# 이동, 왼쪽, 오른쪽
dict['U'] = [[-1,0], 'L', 'R']
dict['D'] = [[1,0], 'R', 'L']
dict['L'] = [[0,-1], 'D', 'U']
dict['R'] = [[0,1], 'U', 'D']

time = 0 
x, y = 0, 0
d = 'R'
body = deque()
body.append([0, 0])

while True:
    time += 1
    dx, dy = dict[d][0]
    x, y = x+dx, y+dy 
    
    if [x,y] in body or (not 0<=x<n) or (not 0<=y<n):
        break
    
    body.append([x, y])
    
    if board[x][y] == 1:
        board[x][y] = 0 
    else:
        body.popleft()
        
    if time in direction:
        if direction[time] == 'L':
            d = dict[d][1]
        else:
            d = dict[d][2]

print(time)
 