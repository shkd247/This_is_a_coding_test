
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

# 노드, 간선 
v, e = map(int, input().split())
global parent
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i
    
for _ in range(e):
    a, b = map(int, input().split())
    union(a, b)

print('원소가 속한 집합')
for i in range(1, v+1):
    print(find(i), end=' ')

print('부모 테이블 ')
for i in range(1, v+1):
    print(parent[i], end=' ')