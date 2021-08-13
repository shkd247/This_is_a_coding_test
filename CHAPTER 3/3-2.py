# 92p. 큰 수의 법칙 

def mysolution(): 
    n, m, k = map(int, input().split())
    nlist = list(map(int, input().split()))

    nlist.sort()

    max = nlist[n-1]
    premax = nlist[n-2]
    res = 0

    for i in range(m):
        if i%k==0 and i!=0:
            res+=premax
        else:
            res+=max

    print(res)


def solution(): 
    n, m, k = map(int, input().split())
    nlist = list(map(int, input().split()))

    nlist.sort()

    first = nlist[n-1]
    second = nlist[n-2]
    res = 0
    res = int(m/k)*k*first + int(m%k)*second
    print(res)


if __name__ == "__main__":
    mysolution()
