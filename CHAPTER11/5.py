# # 볼링공 갯수, 공의 최대 무게 
# n, m = map(int, input().split())
# balls = list(map(int, input().split()))

# res = 0 

# for i in range(len(balls)):
#     for j in range(i+1, len(balls)):
#         if balls[i] != balls[j]:
#             res += 1
            
# print(res)


from collections import defaultdict

# 볼링공 갯수, 공의 최대 무게 
n, m = map(int, input().split())
balls = list(map(int, input().split()))

arr = defaultdict(int)

for ball in balls:
    arr[ball] += 1
    
res = 0 

for ball in balls:
    n -= arr[ball]
    res += arr[ball]*n
    
print(res)
    