import heapq, sys
from collections import defaultdict

input = sys.stdin.readlines
INF = int(1e9)

# 노드 개수, 간선 개수 
n, m = map(int, input().split())
start = int(input)

graph = defaultdict(list)
distance = [INF] * (n+1)

# a->b 노드 이동 비용 c
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    
q = []
heapq.heappush(q, (0, start))
distance[start] = 0 

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if distance[i[0]] > cost:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
            
            
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


