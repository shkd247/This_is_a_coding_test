
def mysolution():           
    n, m = map(int, input().split())
    nums  = list(map(int, input().split()))
    num = min(nums)
    
    while True:
        def minus(n):
            if n-num<0:
                return 0
            else:
                return n-num
        total = sum(list(map(minus, nums)))
        if total>m:
            num+=1
        else:
            break
    
    print(num)
            
    
def solution():
    n, m = map(int, input().split())
    nums  = list(map(int, input().split()))
    start, end = 0, max(nums)
    mid = 0 
    
    res = 0 
    while start<=end:
        mid = (start+end)//2
        def minus(n):
            if n-mid<0:
                return 0
            else:
                return n-mid
        total = sum(list(map(minus, nums)))
        if total == m:
            break
        
        if total<m:
            end = mid-1
        else:
            start = mid+1
            res = total
                
    print(reversed)
    
if __name__ == "__main__":
    mysolution() 