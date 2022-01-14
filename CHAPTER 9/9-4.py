import sys

input = sys.stdin.readlines
INF = int(1e9)

# 회사 개수, 경로 개수 
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0 
    
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# k번 회사 방문 후 x번 회사 가야함
x, k = map(int, input().split())

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
            
answer = graph[1][k] + graph[k][x]

if answer>=INF:
    print(-1)
else:
    print(answer)