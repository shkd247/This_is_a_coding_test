n = int(input())
coins = list(map(int, input().split()))
coins.sort()

res = 1
for coin in coins:
    if res<coin:
        break
    res += coin

print(res)