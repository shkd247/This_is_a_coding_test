
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
parent= [0] * (n+1)

for i in range(n+1):
    parent[i] = i
    
for _ in range(m):
    o, a, b = map(int, input().split())
    if o == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
            
