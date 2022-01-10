
def mysolution():           
    n = int(input())
    dp = [1e9]*(n+1)
    dp[2] = 1
    dp[3] = 2
    for i in range(4,n+1):
        dp[i] = dp[i-1]+1
        if i%5==0:
            dp[i] = min(dp[i//5]+1, dp[i])
        if i%3==0:
            dp[i] = min(dp[i//3]+1, dp[i])
        if i%2==0:
            dp[i] = min(dp[i//2]+1, dp[i])
                
    print(dp[n])
    
def solution():
    n = int(input())
    dp = [0]*(n+1)
    for i in range(2,n+1):
        dp[i] = dp[i-1]+1
        if i%2==0:
            dp[i] = min(dp[i//2]+1, dp[i])
        if i%3==0:
            dp[i] = min(dp[i//3]+1, dp[i])
        if i%5==0:
            dp[i] = min(dp[i//5]+1, dp[i])    
            
    print(dp)
    print(dp[n])  
    
if __name__ == "__main__":
    mysolution() 