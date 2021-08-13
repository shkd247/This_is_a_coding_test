
def mysolution(): 
    n, m = map(int,input().split())
    min = 0 
    for i in range(n):
        line = list(map(int, input().split()))
        line.sort()
        if min<line[0]:
            min = line[0]
    print(min)


def solution():
    n, m = map(int,input().split())
    res = 0 
    for i in range(n):
        line = list(map(int, input().split()))
        min_value = min(line)
        res = max(res, min_value)
    print(min)


if __name__ == "__main__":
    mysolution()