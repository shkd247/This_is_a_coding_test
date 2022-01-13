
from re import T


def mysolution():           
    n, m = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    coins.sort(reverse=True)
    print(coins)
    d = [-1] * (m+1)
    
    for i in range(1, m+1):
        for coin in coins:
            if i==coin:
                d[i] = 1
                break
            if d[i-coin] != -1:
                d[i] = d[i-coin] + 1
                break
            
    print(d[m])
    
    
def solution():
    n, m = map(int, input().split())
    array = [int(input()) for _ in range(n)]
    
    d = [10001] * (m+1)
    
    d[0] = 0 
    for i in range(n):
        for j in range(array[i], m+1):
            if d[j-array[i]] != 10001:
                d[j] = min(d[j], d[j-array[i]]+1)
                
    if d[m] == 10001:
        print(-1)
    else:
        print(d[m])
    
if __name__ == "__main__":
    mysolution() 