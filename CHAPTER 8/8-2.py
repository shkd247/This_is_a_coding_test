
def mysolution():           
    n = int(input())
    stores = list(map(int, input().split()))
    
    if n<3:
        return max(stores)
    
    for i in range(3, n):
        stores[i] = max(stores[i-2]+stores[i], stores[i-1])
        
    print(stores[-1])
    
    
def solution():
    n = int(input())
    stores = list(map(int, input().split()))
    d = [0]*(n+1)
    
    d[0] = stores[0]
    d[1] = max(stores[0], stores[1])
    for i in range(2, n):
        d[i] = max(d[i-2]+stores[i], d[i-1])
        
    print(d[-1])
    
if __name__ == "__main__":
    mysolution() 