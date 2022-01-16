
def find(x):
    if parent[x] != x:
        parent[x] = find(x)
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a

v, e = map(int, input().split())
global parent
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i  

edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

result = 0 
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += cost
        
print(result)