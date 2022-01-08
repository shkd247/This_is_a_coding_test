def mysolution():                                                                                      
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    for _ in range(k):
        a_idx = a.index(min(a))
        b_idx = b.index(max(b))
        
        a[a_idx], b[b_idx] = b[b_idx], a[a_idx]
        
    print(sum(a))
        
def solution():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort(reverse=True)
    
    for i in range(k):
        if a[i]<b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break
    
    print(sum(a))
    
if __name__ == "__main__":
    mysolution()