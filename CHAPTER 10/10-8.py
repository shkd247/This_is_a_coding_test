def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a>b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())
global parent
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

edges = []

for _ in range(m):
    a, b, c = map(int, input().split())     
    edges.append((c, a, b))
    
edges.sort()

last = 0 
result = 0 
for edge in edges:
    c, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += c
        last = c 

print(result-last)
    