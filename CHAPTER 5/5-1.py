
def mysolution():
    n, m = map(int, input().split())
    board  = [list(input().strip()) for _ in range(n)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def check(x, y):
        board[x][y] = '1'
        for i in range(4):
            _x, _y = x+dx[i], y+dy[i] 
            if 0<=_x<n and 0<=_y<m and board[_x][_y]=='0':
                check(_x,_y)
                
    ans = 0 
    for i in range(n):
        for j in range(m):
            if board[i][j]=='0':
                check(i, j)
                ans += 1
    
    print(ans)
                                                                                                         

def solution():
    n, m = map(int, input().split())
    graph  = [list(map(int, input())) for _ in range(n)]
    
    def dfs(x, y):
        if 0<=x<n and 0<=y<m and graph[x][y]==0:
            graph[x][y]=1
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
        return False
        
    result = 0 
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1 

if __name__ == "__main__":
    mysolution()