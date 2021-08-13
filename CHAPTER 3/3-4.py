
def mysolution(): 
    n, k = map(int, input().split())
    count = 0
    while n>=1:
        while n%k !=0 and n>1: 
            n-=1
            count+=1
        
        if n==1:
            break

        n //= k
        count+=1
    print(count)

def solution():
    n, k = map(int, input().split())
    result = 0
    while n>=k:
        while n % k != 0:
            n-=1
            result+1
        n//k        
        result+=1

    while n>1:
        n -= 1
        result +=1

    print(result)

if __name__ == "__main__":
    mysolution()