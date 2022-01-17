from collections import defaultdict, deque
import copy

def mysolution():
    n = int(input())
    times = [0] * (n+1)
    subject = defaultdict(list)

    for i in range(1, n+1):
        line = list(map(int, input().split()))
        times[i] = line[0]
        for l in range(1, len(line)-1):
            subject[i].append(line[l])

    for i in range(1, n+1):
        for s in subject[i]:
            times[i] += times[s]
            
    for i in range(1, n+1):
        print(times[i])
        
def solution():
    v = int(input())
    indegree = [0] * (v+1)
    graph = defaultdict(list)
    time = [0] * (v+1)
    
    for i in range(1, v+1):
        data = list(map(int, input().split()))
        time[i] = data[0]
        for x in data[1:-1]:
            indegree[i] += 1
            graph[x].append(i)
            
    result = copy.deepcopy(time)
    q = deque()
    
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1 
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1, v+1):
        print(result[i])