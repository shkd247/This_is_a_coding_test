from collections import deque, defaultdict

# 노드, 간선
v, e = map(int, input().split())
# 진입차수
indegree =[0] * (v+1)
graph = defaultdict(list)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

result = []
q = deque()

for i in range(1, v+1):
    if indegree[i] == 0:
        q.append(i)
        
while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)
            
for i in result:
    print(i,end=' ')
