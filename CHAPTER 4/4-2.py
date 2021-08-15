
def mysolution():
    n = int(input())

    cnt = 0

    for h in range(n+1):
        if '3' in str(h):
            cnt+=3600
            continue
        for m in range(60):
            if '3' in str(m):
                cnt+=60
                continue
            for s in range(60):
                if '3' in str(s):
                    cnt+=1

    print(cnt)

def solution():
    h = int(input())

    count=0
    for i in range(h+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i)+str(j)+str(k):
                    count+=1
    print(count)

if __name__ == "__main__":
    mysolution()