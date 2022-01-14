from cmath import cos
from collections import defaultdict
import heapq

def mysolution():        
    # 도시 개수, 통로 개수, 메시지 보내고자 하는 도시 
    n, m, c = list(map(int, input().split()))
    
    graph = defaultdict(list)
    for _ in range(m):
        # x->y 통로 있고 메시지 전달하는데 z시간이 걸림
        x, y, z = map(int, input().split())
        graph[x].append([y, z])
    
    visited = [False] * (n+1)
    cost = 0 
    q = []
    q.append(c)
    
    while q:
        start = q.pop()
            
        if visited[start] == True:
            continue
            
        visited[start] = True
            
        for des, des_cost in graph[start]:
            if visited[des] == False:
                cost = max(cost, cost+des_cost)
                q.append([des, cost+des_cost])    
                    
    print(visited.count(True)-1, cost)
    
def solution():
    INF = int(1e9)
    
    # 도시 개수, 통로 개수, 메시지 보내고자 하는 도시 
    n, m, start = list(map(int, input().split()))
    
    graph = defaultdict(list)
    for _ in range(m):
        # x->y 통로 있고 메시지 전달하는데 z시간이 걸림
        x, y, z = map(int, input().split())
        graph[x].append([y, z])
    
    distance = [INF]*(n+1)
    
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0 
    
    while q:
        cost, now = heapq.heappop()
        if distance[now] < cost:
            continue
        for i in graph[now]:
            if distance[i[0]] > cost+i[1]:
                distance[i[0]] = cost+i[1]
                heapq.heappush(q, [distance[i[0]], i[0]])
                
    city, time = 0, 0 
    for i in distance:
        if i != INF:
            city += 1
            time = max(time, i) 
            
    print(city-1, time)
            
        
        
if __name__ == "__main__":
    mysolution() 
        